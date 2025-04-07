import pygame
import locale
import random as rnd
import subprocess
import sys
import csv
import os
from configparser import ConfigParser
from assistant_ai import AssistAI
from config import ConfigTXT
from persons import PersonRPG

def get_data(path):
    try:
        base_path = os.path.join(sys._MEIPASS, "data");
    except:
        base_path = os.path.abspath("./data");
    return os.path.join(base_path, path);
def get_language(language:str|None=None):
    _lang = ConfigParser();
    if language is None:
        locale_lang = locale.getlocale()[0];
        ini_lang = locale_lang.split("_")[0];
        try:
            _lang.read(get_data(f"langs/{ini_lang}.ini"), "utf-8");
        except:
            _lang.read(get_data("langs/en.ini"), "utf-8");
    else:
        _lang.read(get_data(f"langs/{language}.ini"), "utf-8");
    return _lang;
def clear():
    os.system('cls' if os.name == 'nt' else 'clear');
def get_param(command:str):
    param = "";
    for i in command.split():
        if i == command.split()[1]:
            param += i;
        if i != command.split()[0] and i != command.split()[1]:
            param += " ";
            param += i;
    return param;
def save_dice(seed, result):
    with open("dice.csv", "a", newline='') as file:
        csv.writer(file).writerow([f"Resultado: {result}", f"Seed: {seed}"]);
def play_audio(audio:str|None="audio.mp3"):
    try:
        subprocess.run([config.get('DIR-SOUNDPAD'), '-rc', 'DoPlaySound(1)']);
    except:
        pygame.mixer.music.unload();
        pygame.mixer.music.load(audio);
        pygame.mixer.music.play();

pygame.mixer.init();
config = ConfigTXT({"API-KEY":"str,none", "DIR-SOUNDPAD":"str,none", "VOICE-ID":"str,none", "LANGUAGE":"str,none"});
if config.get("LANGUAGE") == "none":
    lang = get_language();
else:
    lang = get_language(config.get("LANGUAGE"));
assistant = AssistAI(lang.get("Prompt", "Assist"));
while True:
    clear();
    _input = input(lang.get("Command", "List").format("\n", ";")+" ");
    clear();
    match _input.split()[0]:
        case "assist":
            print(lang.get("Command", "Response"), assistant.response(get_param(_input)));
        case "setperson":
            person = PersonRPG(_input.split()[1], lang);
            if config.get("API-KEY") == "none":
                person_ai = AssistAI(f"{lang.get("Prompt", "Person")} {person.list()}", False);
            if config.get("API-KEY") != "none":
                person_ai = AssistAI(f"{lang.get("Prompt", "Person")} {person.list()}", False, api_key=config.get("API-KEY"));
            print(person.list());
        case "person":
            try:
                if config.get("API-KEY") == "none":
                    print(f"{person.name}:", person_ai.response(get_param(_input)));
                if config.get("API-KEY") != "none":
                    response = person_ai.response(get_param(_input));
                    try:
                        person_ai.text_to_speech(person.voice, response);
                        person_ai.save_audio();
                        play_audio();
                    except:
                        print(lang.get("Error", "PersonVoice"));
                    print(f"{person.name}:", response);
            except:
                print(lang.get("Error", "PersonNotSelect"));
        case "d":
            dice_roll = [];
            seed = rnd.randint(0,1000000);
            rnd.seed(seed);
            print(lang.get("Dice", "Seed"), seed);
            for _ in range(int(_input.split()[1])):
                dice_roll.append(rnd.randrange(1, int(_input.split()[2])+1));
            dice_print = "";
            dice_result = 0;
            for i in dice_roll:
                if i == dice_roll[len(dice_roll)-1]:
                    dice_print += f"{i} ";
                else:
                    dice_print += f"{i},";
                dice_result += i;
            dice_print += f"| [{dice_result}] {lang.get("Dice", "Result")}";
            save_dice(seed, dice_result);
            print(dice_print);
        case "textaudio":
            try:
                speech = AssistAI(chat_save=False, api_key=config.get("API-KEY"));
                try:
                    speech.text_to_speech(person.voice, get_param(_input));
                except:
                    speech.text_to_speech(config.get("VOICE-ID"), get_param(_input));
                speech.save_audio();
                play_audio();
            except:
                if config.get("API-KEY") == "none":
                    print(lang.get("Error", "NotDefined").format("API-KEY"));
                elif config.get("VOICE-ID") == "none":
                    print(lang.get("Error", "NotDefined").format("VOICE-ID"));
                else:
                    print(lang.get("Error", "NotValidTwo").format("API-KEY", "VOICE-ID"));
        case _:
            print(lang.get("Error", "ComNotExist"));
    input();
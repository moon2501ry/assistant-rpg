import pygame
import random as rnd
import subprocess
import csv
import os
from assistant_ai import AssistAI
from config import ConfigTXT
from persons import PersonRPG

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

config = ConfigTXT({"API-KEY":"str,none", "DIR-SOUNDPAD":"str,none", "VOICE-ID":"str,none"});
assistant = AssistAI("Você será um assistente para RPGs");
while True:
    os.system('cls' if os.name == 'nt' else 'clear');
    _input = input("Lista de comandos:\n  assist [msg] - Pergunte para o assistente;\n  setperson [name_or_id] - Seleciona um personagem;\n  person [msg] - Imita o personagem selecionado;\n  textaudio [text] - Faz a voz de um npc;\n  d [num_of_dice] [num_dice] - Rola [num_of_dice] dados de [num_dice] dados;\n\nInput> ");
    os.system('cls' if os.name == 'nt' else 'clear');
    match _input.split()[0]:
        case "assist":
            print("Resposta:", assistant.response(get_param(_input)));
        case "setperson":
            person = PersonRPG(_input.split()[1]);
            if config.get("API-KEY") == "none":
                person_ai = AssistAI(f"Imite esse personagem de RPG: {person.list()}", False);
            if config.get("API-KEY") != "none":
                person_ai = AssistAI(f"Imite esse personagem de RPG: {person.list()}", False, api_key=config.get("API-KEY"));
            print(person.list());
        case "person":
            try:
                if config.get("API-KEY") == "none":
                    print(f"{person.name}:", person_ai.response(get_param(_input)));
                if config.get("API-KEY") != "none":
                    response = person_ai.response(get_param(_input));
                    person_ai.text_to_speech(person.voice, response);
                    person_ai.save_audio();
                    play_audio();
                    print(f"{person.name}:", response);
            except:
                print("Nenhum personagem selecionado!");
        case "d":
            dice_roll = [];
            seed = rnd.randint(0,1000000);
            rnd.seed(seed);
            print("Seed:", seed);
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
            dice_print += f"| [{dice_result}] foi o resultado!";
            save_dice(seed, dice_result);
            print(dice_print);
        case "textaudio":
            try:
                try:
                    person_ai.text_to_speech(person.voice, get_param(_input));
                    person_ai.save_audio();
                    play_audio();
                except:
                    speech = AssistAI(chat_save=False, api_key=config.get("API-KEY"));
                    speech.text_to_speech(config.get("VOICE-ID"), get_param(_input));
                    speech.save_audio();
                    play_audio();
            except:
                print("API-KEY not seted or VOICE-ID not seted!")
        case _:
            print("Comando não existe");
    input();
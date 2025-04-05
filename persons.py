import csv
from language import LangINI

class PersonRPG:
    def __init__(self, name_or_id, lang:str|None=None):
        if lang is None:
            self.lang = LangINI();
        else:
            self.lang = LangINI(lang);
        def open_file():
            with open("persons.csv", 'r', encoding="utf-8", newline='') as file:
                for i in csv.reader(file, delimiter='|'):
                    if i[0] == name_or_id or i[1] == name_or_id:
                        self.name = i[1];
                        self.lore = i[2];
                        self.character = i[3];
                        self.age = i[4];
                        self.gender = i[5];
                        self.voice = i[6];
        try:
            open_file();
        except:
            with open("persons.csv", 'w', encoding="utf-8", newline='') as file:
                csv.writer(file, delimiter='|').writerow(["ID",self.lang.ini.get("Person","Name"),"Lore",self.lang.ini.get("Person","Character"),self.lang.ini.get("Person","Age"),self.lang.ini.get("Person","Gender"),"VoiceID"]);
                csv.writer(file, delimiter='|').writerow([0,self.lang.ini.get("PersonTemplate","Name"),self.lang.ini.get("PersonTemplate","Lore"),self.lang.ini.get("PersonTemplate","Character"),25,self.lang.ini.get("PersonTemplate","Gender"),"t0e1s2t3e"]);
            while True:
                if input(self.lang.ini.get("Person","EditCsv").format("\n")) == self.lang.ini.get("Person","Yes"):
                    break;
            open_file();

    def list(self):
        return f"{self.lang.ini.get("Person","Name")}: {self.name}; Lore: {self.lore}; {self.lang.ini.get("Person","Character")}: {self.character}; {self.lang.ini.get("Person","Age")}: {self.age}; {self.lang.ini.get("Person","Gender")}: {self.gender}";

if __name__ == "__main__":
    print("U can't use this python file like main");
import csv

class PersonRPG:
    def __init__(self, name_or_id, strings):
        self.strings = strings;
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
                csv.writer(file, delimiter='|').writerow(["ID",strings.get("Person","Name"),"Lore",strings.get("Person","Character"),strings.get("Person","Age"),strings.get("Person","Gender"),"VoiceID"]);
                csv.writer(file, delimiter='|').writerow([0,strings.get("PersonTemplate","Name"),strings.get("PersonTemplate","Lore"),strings.get("PersonTemplate","Character"),25,strings.get("PersonTemplate","Gender"),"t0e1s2t3e"]);
            while True:
                if input(strings.get("Person","EditCsv").format("\n")) == strings.get("Person","Yes"):
                    break;
            open_file();

    def list(self):
        return f"{self.strings.get("Person","Name")}: {self.name}; Lore: {self.lore}; {self.strings.get("Person","Character")}: {self.character}; {self.strings.get("Person","Age")}: {self.age}; {self.strings.get("Person","Gender")}: {self.gender}";

if __name__ == "__main__":
    print("U can't use this python file like main");
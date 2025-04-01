import csv

class PersonRPG:
    def __init__(self, name_or_id):
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
                csv.writer(file, delimiter='|').writerow(["ID","Name","Lore","Character","Age","Gender","VoiceID"]);
                csv.writer(file, delimiter='|').writerow([0,"Teste","Personagem de teste","Sem Personalidade",25,"Masculino","t0e1s2t3e"]);
            while True:
                if input("Edit 'persons.csv' template, please.\nHave you edited it yet? | y or n>") == "y":
                    break;
            open_file();

    def list(self):
        return f"Nome: {self.name}; Lore: {self.lore}; Características: {self.character}; Idade: {self.age}; Gender: {self.gender}";

if __name__ == "__main__":
    print("U can't use this python file like main");
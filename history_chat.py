import csv

class History:
    def __init__(self, content:str|None=None):
        if content is not None:
            self.chat = [{"role": "system", "content": content}];
        else:
            self.chat = [];
    def add(self, content:str, role:str|None="user"):
        self.chat.append({"role": role, "content": content});
    def add_response(self, response):
        self.chat.append({"role": str(response.choices[0].message.role), "content": str(response.choices[0].message.content)});
    def print(self):
        '''Print Chat History'''
        _print = "CHAT - HISTORY\n--------------\n";
        for message in self.chat:
            _print += f"ROLE: {message["role"]} | CONTENT: {message["content"]};\n";
        print(_print);
        return _print;
    def save(self, csv_file:str|None='chat.csv'):
        '''
        Save **CSV** file with **Chat History**

        ***csv_file*** is the directory for csv file
        '''
        with open(csv_file, "w", newline='', encoding="utf-8") as file:
            csv.writer(file).writerow(["Role","Content"]);
            for message in self.chat:
                csv.writer(file).writerow([message["role"],message["content"]]);
    def open(self, csv_file:str|None='chat.csv'):
        '''
        Open **CSV** file with **Chat History**

        ***csv_file*** is the directory of the csv file
        '''
        with open(csv_file, "r", newline='', encoding="utf-8") as file:
            rows = csv.reader(file);
            for row in rows:
                if row[0] != "Role":
                    self.add(row[1], row[0]);

if __name__ == "__main__":
    print("U can't use this python file like main");
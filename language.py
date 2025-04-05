from configparser import ConfigParser
import locale

class LangINI:
    def __init__(self, language:str|None=None):
        if language is None:
            lang = locale.getlocale()[0];
            self.ini = ConfigParser();
            match lang:
                case "pt_BR":
                    self.ini.read("langs/pt.ini", "utf-8");
                case "ja_JP":
                    self.ini.read("langs/jp.ini", "utf-8")
                case _:
                    self.ini.read("langs/en.ini", "utf-8");
        else:
            self.ini = ConfigParser();
            self.ini.read(f"langs/{language}.ini", "utf-8");
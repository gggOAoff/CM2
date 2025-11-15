import xml.etree.ElementTree as ET

class ConfigParser:
    def __init__(self, Path = "Config.xml"):
        self.Path = Path
        self.Config = {}
        self.AllTags = {
            "package": ("name", "version"), 
            "repository": ("mode", "test_path", "url"),
            "output": ("filename", ),
            "filters": ("substring", )
        }
        self.RepTag = ["mode", "test_path", "url"]
    
    def Parse(self):
        Root = ET.parse(self.Path).getroot()
        for i in self.AllTags.keys():
            for j in self.AllTags[i]:
                self.Config[j] = self.Get(self.Get(Root, i, Text = False), j)
        if self.Config["test_path"] is not None:
            if self.Config["mode"] is None:
                raise ValueError("Отсутствует режим для тестового репозитория")
        else:
            if self.Config["url"] is None:
                raise ValueError("Отстутствует ссылка на репозиторий")
    
    def Get(self, Parent, Tag, Text = True):
        T = Parent.find(Tag)
        if T is None:
            if Tag not in self.RepTag:
               raise ValueError(f"Тег \"{Tag}\" не найден")
            return None if Text else Parent
        if Text:
            T = T.text
            if T is None and Tag not in self.RepTag:
                raise ValueError(f"Значение тега \"{Tag}\" не может быть пустым")
        return T
    
    def Print(self):
        for i in self.AllTags.keys():
            print(f"{i}:")
            for j in self.AllTags[i]:
                if self.Config[j] is not None: 
                    print(f"    {j} = {self.Config[j]}")
            print()

Parser = ConfigParser()
Parser.Parse()
Parser.Print()
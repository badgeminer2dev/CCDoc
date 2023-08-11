import re
class File:
    def __init__(self,filename:str,content:str) -> None:
        self.modules:dict[str,Module] = {}
        self.classes:dict[str,Class] = {}
        self.filename = filename
        for i in re.findall(r"(--- @module \w+)",content):
            n = str(i).split(" ")[2]
            self.modules[n] = Module(n,filename,content)
        for i in re.findall(r"(--- @class \w+)",content):
            n = str(i).split(" ")[2]
            self.classes[n] = Class(n,filename,content)

class Class:
    def __init__(self,name,file,content) -> None:
        self.name = name
        self.file = file
        pattern = re.compile(f"(--- .+\n)?(function ({name})\\.)(\\w+)(\\((\\w+(:\\w+)?,?)*\\))")

class Module:
    def __init__(self,name,file,content) -> None:
        self.name = name
        self.file = file
        pattern = re.compile((r"(((\t| {4})*--- ?.+\n)*)((\t| {4})*function ({MODULENAME})\.)(\w+)(\(( ?\w+,?)*\))").replace("{MODULENAME}",name))
        self.funcs:dict[str,Funct] = {}
        for match in pattern.finditer(content):
            desc = match.group(1)
            if not desc: desc = ""
            desc = desc.removeprefix("--- ").removesuffix("\n")
            self.funcs[match.group(7)] = Funct(match.group(7),file,match.group(8),desc)
        

class Funct:
    def __init__(self,name,file,args,desc) -> None:
        self.args = args
        self.desc = desc

class Parser:
    def __init__(self,fin,files:list) -> None:
        self.files:dict[str,File] = {}
        for F in files:
            with open(fin+"/"+F) as f:
                self.files[F] = File(F,f.read())
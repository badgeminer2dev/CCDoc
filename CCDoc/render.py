import jinja2,shutil
from .parse import File
def render(title,files:list[File],output:str):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("assets/"))
    fileNames = []
    fc = 0
    mc = 0
    Fc = 0
    for F in files:
        fileNames.append(F.filename)
    for F in files:
        fc +=1
        modus = []
        for n,m in F.modules.items():
            mc += 1
            M = {"name":n,"funcs":[]}
            for N,f in m.funcs.items():
                Fc += 1
                desc = str(f.desc).replace("\n","<br>").replace("---","")
                M["funcs"].append({"name":N,"args":f.args,"desc":desc,"sdesc":desc.split("<br>")[0]})
            modus.append(M)
        template = environment.get_template("template.html")
        with open(output+"/"+F.filename+".html","w") as f:
            f.write(template.render(title=title,files=fileNames,modules=modus).replace("ś","¶"))
    shutil.copyfile("assets/css.css",f"{output}/css.css")
    return fc,mc,Fc
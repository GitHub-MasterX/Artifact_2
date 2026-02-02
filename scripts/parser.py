import re
from pathlib import Path

SYSCALL_RE = re.compile(r'^\s*(?:\d+\s+)?([a-zA-Z_][a-zA-Z0-9_]*)\(')
BASE = Path.home() / "Artifact2"
def pars(x):
    temp=[]
    with open(x,'r',encoding="utf-8", errors='replace') as file:
        for line in file:
            line = re.sub(r'<unfinished \.\.\.>',' ',line)
            line = re.sub(r'<\.\.\. .* resumed>',' ',line)
            m=SYSCALL_RE.match(line)
            if m:
                temp.append(m.group(1))
    assert len(temp)>0
    with open(BASE / "scripts" / "data_structures.py","a") as f:
        scenario=x.parents[1].name
        mode=x.parents[0].name
        if x.stem == "combine":
            scope = "combined"
        else:
            scope = "raw"
        name=f"{scenario}_{mode}_{scope}"
        f.write(f"{name} = {temp}\n")

for item in (BASE / "data").iterdir():
    if item.is_dir():
        for i in item.iterdir():
            if i.name=="multi":
                if i.is_dir():
                    for t in i.iterdir():
                        pars(t)
            if i.name=="single":
                if i.is_dir():
                    for t in i.iterdir():
                        if t.name=="combine.txt":
                            pars(t)
    elif item.is_file():
        pars(i)

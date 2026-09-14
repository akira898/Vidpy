import os 
import main
from main import projectToRun
script={}
inLine=1
carpetToCheck=os.path.join("project",projectToRun)
if not os.path.exists(os.path.join(carpetToCheck,"script.txt")):
    os.makedirs("project")
    with open(os.path.join(carpetToCheck,"script.txt"), "w") as f:
        f.write("Character Adam as a")
for filename in os.listdir(carpetToCheck):
    if filename.endswith(".txt"):
        with open(os.path.join(carpetToCheck, filename), "r") as f:
            content = f.read()
            for line in content.splitlines():
                if not line.strip():
                    inLine+=1
                    continue
                line=line.split()
                script[inLine]=line
                inLine+=1
#belive it or not, thsi doesn't break anything
import AST
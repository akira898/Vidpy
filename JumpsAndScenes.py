sceneData={}
import os
class scenes:
    def __init__(self,name,line,jump):
        self.name=name
        self.line=line
        self.jump=jump
def ScenesManagment():
    with open ("Scene.txt","r",encoding="utf-8")as scene:
        for line in scene:
            words=line.split()
            sceneData[words[0]]=scenes(words[0],int(words[1]),0)
            print(sceneData)
            if os.path.exists("Jump to"+words[0]+".txt"):
               with open ("Jump to"+words[0]+".txt","r",encoding="utf-8")as jump:
                   for line in jump:
                       jumper=line.split()
                       sceneData[words[0]].jump=int(jumper[0])
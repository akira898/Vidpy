from refactored import script
imagesInGame={}
backgroundsIn={}
import os
import main
from main import projectToRun
from Visuals import visualGestore
import time
WorksAsName=[]
whichDialogue=0
jumpsList=[]
scenesInGame=[]
names=[]
dialogueInGame=[""]
if os.path.exists("dialgue.txt"):
    with open ("dialgue.txt","r",encoding="utf-8") as Dial:
        dialogueInGame=Dial.read().splitlines()
        
        print ("dialogueInGame",dialogueInGame)
def errors():
    print("error")
def Character(line):
    addName=[]
    asCheck=False
    for i in script[line][1:]:
        if i=="as":
            names.append(" ".join(addName))
            lookingAtWord=script[line].index("as")+1
            asCheck=True
            break

        else:
            addName.append(i)
    print(names)
    print("emote")
    if not asCheck or lookingAtWord >= len(script[line]):
        print("line: ",line," you need to provide an alias")
        return 
    if script[line][lookingAtWord] in WorksAsName:
            print("errrr")
            return
    elif script[line][lookingAtWord]=="":
        print("Line:",line,"you need to provide an alias")
    else:
            print("Guess who is clibing the door")
            WorksAsName.append(script[line][lookingAtWord])
            print(WorksAsName)
       
def speak(line):
    global whichDialogue
    global dialogueInGame
    global WorksAsName
    dialgue=" ".join(script[line][1:])
    if dialgue not in dialogueInGame :
            characterIn=WorksAsName.index(script[line][0].rstrip(':'))
            if whichDialogue<len(dialogueInGame) and len(dialogueInGame)>0:
                print("delete")
                del dialogueInGame[whichDialogue]
                dialogueInGame.append(dialgue)
                print (dialogueInGame)
                with open ("dialgue.txt","w",encoding="utf-8") as Dial:
                    for line in dialogueInGame:
                        print(line)
                        Dial.writelines(line + "\n")
                del dialogueInGame[whichDialogue]
                print(Dial)
            else:
                print(dialgue)
                with open("dialgue.txt", "a", encoding="utf-8") as Dial:
                    Dial.write(dialgue+ "\n")
    else:
        print("line in game")
    print(len(dialogueInGame))
    print(whichDialogue)
    whichDialogue+=1

    
def image(line):
    position=["left","right","center"]
    print("conditions")
    global whichDialogue
    global imagesInGame
    global backgroundsIn
    positions=["center","left","right"]
    if script[line][0]== "show":
        print("image to show")
        imagesPath=os.path.join("projects",projectToRun+"Vidpy","Images","Images And whenToputThem.txt")
        with open(imagesPath, "a", encoding="utf-8") as iawtt:
            if script[line][1] in imagesInGame:
                imagesInGame[script[line][1]]+=1
            else:
                imagesInGame[script[line][1]]=0
            if len(script[line])>3:
                if script[line][3] in positions and script[line][2]=="at":
                    iawtt.write("show " + script[line][1] +  " " + str(whichDialogue)+" "+ script[line][3] +" "+str(imagesInGame[script[line][1]])+"\n")
                else:
                    print("Line: ",line,"To set the image direction you need: at + position")
                    return

            else:
                iawtt.write("show " + script[line][1] +" " + str(whichDialogue)+" "+str(imagesInGame[script[line][1]])+"\n")
        

    elif script[line][0]== "hide" and  script[line][1] in imagesInGame:
        hidePath=os.path.join("projects",projectToRun+"Vidpy","Images","limit" + script[line][1] +" " +str(imagesInGame[script[line][1]])+".txt")
        dialogueMaxi = whichDialogue
        with open(hidePath, "w", encoding="utf-8") as limit:
            limit.write(str(dialogueMaxi)+" "+"\n")
        print("fel")
        visualGestore()
    elif script[line][0]== "background" and len(script[line])>1:
        if script[line][1] in imagesInGame:

            print("Line: ",line," you can't use a background that is already in use ") 
        backgroundsIn[script[line][1]]=0
        backgroundPath=os.path.join("projects",projectToRun+"Vidpy","Images","backgrounds.txt")
        with open (backgroundPath,"a",encoding="utf-8") as backgrounds:
            backgrounds.write(script[line][1]+" "+str(whichDialogue)+"\n")
    elif script[line][0] == "hide"and len(script[line])>1:
         with open("limit" + script[line][1] +".txt", "w", encoding="utf-8") as limit:
             limit.write(str(dialogueMaxi)+" "+"\n")
    visualGestore()
def toPrint(line):
    print(" ".join(script[line][1:]))
def scenes(line):
    print("")
    global whichDialogue
    global scenesInGame
    scenePath=os.path.join("projects",projectToRun+"Vidpy","jumps","Scene.txt")
    with open ("Scene.txt","a",encoding="utf-8")as scene:
            sceneName = script[line][1].rstrip(":")
            print("Scene: ",sceneName)
            scene.write(sceneName+" "+str(whichDialogue)+"\n")
            scenesInGame.append(sceneName)
def jumps(line):
    #when nit detects a jump makes another fucking  .txt
    global whichDialogue
    global jumpsList
    JumpPath=os.path.join("projects",projectToRun+"Vidpy","jumps","Jump to"+script[line][1]+".txt")
    if not os.path.exists(JumpPath):
        with open (JumpPath,"w",encoding="utf-8")as jump:
            jump.write(str(whichDialogue))
            jumpsList.append(script[line][1])

import clase1
from clase1 import  seeCharcatersAndText
from Visuals import visualGestore
import JumpsAndScenes
from JumpsAndScenes import ScenesManagment
import os
import main
from main import  projectToRun,projectsCarpets
import time 
scenesInGame=["start"]
from errorManagment import errors
from dumpstruck import restart,eraseComplete
names=[]	
positions=["center","left","right"]
WorksAsName=[]
dialogue=False
OnTest=False
whichDialogue=0
dialogueMaxi=0
sceneCommands=["Scene","Jumps"]
toprint=""
visualsCommands=["show","hide","backgrounds"]
imagesInGame=[]
if os.path.exists("projects"+projectToRun+"\\Vidpy"+"\\jumps"+"Scene.txt"):
    restart()
#this is for development
with open ("projects\\"+projectToRun+"\\Vidpy"+"\\jumps"+"\\Scene.txt","w",encoding="utf-8")as scene:
    scene.write("start 0\n")
if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\dialgue.txt") and os.path.exists ("projects\\"+projectToRun+"\\Vidpy"+"\\chractersTurn.txt"):
    os.remove("projects\\"+projectToRun+"\\Vidpy"+"\\dialgue.txt")
    os.remove("projects\\"+projectToRun+"\\Vidpy"+"\\chractersTurn.txt")
if os.path.exists("script.txt" )and OnTest:
    os.remove("script.txt")
if os.path.exists("Vidpy\Images And whenToputThem.txt"):
    os.remove("Vidpy\Images And whenToputThem.txt")
text=""
variables={}
dialogueMaxi = 0
inLine=0
def inputForOperations():
    print("ansked for input")
    variables[words[0]]=input()
def numbers():
    global words 
    global variables
    if line.startswith("Set") and len(words)>3:
                    variables[words[1]]={}
                    print(variables)
                    if words[2]=="to" and not words[3]=="input":
                        
                        variables[words[1]]=words[3]
                    if words[3]=="input":
                        print("ansked for input")
                        variables[words[1]]=input()
                    inLine+=1
    elif  len(words)>3 and words[0] in variables and not words[2] in variables :
                        if words[1]=="plus":
                            if  True:
                                print("hi")
                                try:
                                    firstNumber=int(variables[words[0]])
                                    numberToPluss=int(words[2])
                                    variables[words[0]]=firstNumber+numberToPluss
                                    
                                except ValueError:
                                    print("exception")
                                inLine+=1
                        elif words[2]=="input" and words[1]=="to":
                            variables[words[0]]=input()
                        elif words[1]=="input":
                            print( "you can't reassing a variable to input without an to")
    elif words[0] in variables and words[2] in variables and len(words)>1:
                        print("not now")
                        try:
                                    firstNumber=int(variables[words[0]])
                                    numberToPluss=int(variables[words[2]])
                                    variables[words[0]]=firstNumber+numberToPluss
                                    

                        except ValueError:
                            print("mistake") 
                        inLine+=1
    if words[0] in variables:
                    if words[1]=="to":
                        if words[2] in variables:
                            print("variable")
                        else:
                            print("assing"+words[2])
                            variables[words[0]]=words[2]
                        inLine+=1
def scenes():
    time.sleep(0.5)
    print("")
    global words
    global inLine
    global whichDialogue
    if words[0]=="Scene":
        with open ("projects\\"+projectToRun+"\\Vidpy"+"\\jumps"+"\\Scene.txt","a",encoding="utf-8")as scene:
            sceneName = words[1].rstrip(":")
            scene.write(sceneName+" "+str(whichDialogue)+"\n")
            inLine+=1
            scenesInGame.append(sceneName)
    elif words[0]=="Jumps" and words[1] in scenesInGame :
        with open ("projects\\"+projectToRun+"\\Vidpy"+"\\jumps"+"\\Jump to"+words[1]+".txt","w",encoding="utf-8")as jump:
            jump.write(str(whichDialogue))
            inLine+=1
        

    elif words[0]=="Jumps":
        print("Error in line "+str(inLine)+" Scene not found or not declare")
        main.RunIterpreter=False
def visuals():
    global words
    global dialogueMaxi
    global inLine
    print("conditions")

    if words[0] == "show":
        with open("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\Images And whenToputThem.txt", "a", encoding="utf-8") as iawtt:

            if len(words)>3:
                if words[3] in positions and words[2]=="at":
                    iawtt.write("show " + words[1] +  " " + str(whichDialogue)+" "+ words[3] +"\n")
                    imagesInGame.append(words[1])

            else:
                iawtt.write("show " + words[1] +" " + str(whichDialogue)+"\n")
        inLine += 1
        

    elif words[0] == "hide" and len(words)>1:
        dialogueMaxi = whichDialogue

        with open("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] + ".txt", "w", encoding="utf-8") as limit:
            limit.write(str(dialogueMaxi))

        inLine += 1
        print("fel")
        visualGestore()
    elif words[0] == "backgrounds" and len(words)>1:
        if words[1] in imagesInGame:
            main.RunIterpreter=False
            print("Line: ",inLine," you can't use a background that is already in use ") 
        with open ("backgrounds.txt","a",encoding="utf-8") as backgrounds:
            backgrounds.write(words[1]+" "+str(whichDialogue)+"\n")
while main.RunIterpreter:
    scriptToLookAt=os.path.join("projects", projectToRun, "script.txt")
    if os.path.exists(scriptToLookAt):
        with open(scriptToLookAt,"r", encoding="utf-8") as lines:
            for line in lines:
                print(line)
                line = line.replace(" :", ":")
                line = line.replace(":", ": ")
                words=line.split()
                if not line.strip():
                    inLine+=1
                    continue
                if line.startswith("Character") :
                    try:
                        if words[1] in names:
                            main.RunIterpreter=False
                            errors()
                            break
                        names.append(words[1])
                        print(names)
                        if words[2]=="as":
                            if words[3] in WorksAsName:
                                main.RunIterpreter=False
                                print("Line: ",inLine," two characters can't have the same allias")
                                errors()
                                break
                            WorksAsName.append(words[3]+":")
                            print(WorksAsName)
                            inLine+=1
                    except IndexError:
                        print("Line: ",inLine," a character declaration must be: Character + name+ as + allias")
                        main.RunIterpreter=False
                        errors()
                        break
                elif words[0]=="Character":
                    print("Line: ",inLine," A character must have an allies")
                elif words[0].rstrip(" ") in WorksAsName:
                    speach=" ".join(words[1:])

                    for i in variables:
                        if "{"+i+"}" in speach:
                            print("variable here")
                            speach=speach.replace("{"+i+"}",str(variables[i]))
                    with open ("projects\\"+projectToRun+"\\Vidpy"+"\\dialgue.txt","a",encoding="utf-8")as dilgue:
                        dilgue.write(speach+"\n")
                    positionToLookAt=WorksAsName.index(words[0])
                    nameToWrite=names[positionToLookAt]
                    with open ("projects\\"+projectToRun+"\\Vidpy"+"\\chractersTurn.txt","a",encoding="utf-8")as ch:
                        ch.write(nameToWrite+":\n")
                    whichDialogue+=1
                    inLine+=1
                if line.startswith("Set") or words[0]in variables:
                    numbers()
                if words[0]=="print":
                    toprint=" ".join(words[1:])
                    for i in variables:
                        if "{"+i+"}" in toprint:
                            toprint=toprint.replace("{"+i+"}",str(variables[i]))
                    print(toprint)
                    inLine+=1
                elif words[0] in visualsCommands:
                    visuals()
                elif words[0] in sceneCommands:
                    scenes()
            print("helo")
            ScenesManagment()
            seeCharcatersAndText()
            break
    else:
            print("only")
            with open("script.txt","w",encoding="utf-8")as code:
                code.write("Character Erica as e \n ")
                code.write("Character Conan as c \n")
                code.write("e:prueba \n")
                code.write("print hello, world")
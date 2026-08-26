import clase1
from clase1 import  seeCharcatersAndText
from Visuals import visualGestore
import JumpsAndScenes
from JumpsAndScenes import ScenesManagment
import os
import main
import time 
scenesInGame=[]
names=[]	
WorksAsName=[]
dialogue=False
OnTest=False
whichDialogue=0
dialogueMaxi=0
sceneCommands=["Scene","Jumps"]
toprint=""
visualsCommands=["show","hide"]
#this is for development
with open ("Scene.txt","w",encoding="utf-8")as scene:
	scene.write("start 0\n")
if os.path.exists("dialgue.txt") and os.path.exists ("chractersTurn.txt"):
	os.remove("dialgue.txt")
	os.remove("chractersTurn.txt")
if os.path.exists("script.txt" )and OnTest:
	os.remove("script.txt")
text=""
variables={}
dialogueMaxi = 0
inLine=0
def inputForOperations():
	print("ansked for input")
	variables[words[0]]=input()
def scenes():
	time.sleep(0.5)
	print("")
	global words
	global inLine
	global whichDialogue
	if words[0]=="Scene":
		with open ("Scene.txt","a",encoding="utf-8")as scene:
			scene.write(words[1]+" "+str(whichDialogue)+"\n")
			inLine+=1
			scenesInGame.append(words[1])
			ScenesManagment()
	elif words[0]=="Jumps":
		with open ("Jump to"+words[1]+".txt","w",encoding="utf-8")as jump:
			jump.write(str(whichDialogue))
			inLine+=1
			ScenesManagment()
			for name, item in JumpsAndScenes.sceneData.items():
				print("NAME:", name)
				print("LINE:", item.line)
				print("JUMP:", item.jump)

	elif words[0]=="Jumps":
		print("Error in line "+str(inLine)+" Scene not found or not declare")
		main.RunIterpreter=False
def visuals():
    global words
    global dialogueMaxi
    global inLine

    if words[0] == "show":
        with open("Images And whenToputThem", "a", encoding="utf-8") as iawtt:
            iawtt.write("show " + words[1] + " " + str(whichDialogue) + "\n")

        inLine += 1
        visualGestore()

    elif words[0] == "hide":
        dialogueMaxi = whichDialogue

        with open("limit" + words[1] + ".txt", "w", encoding="utf-8") as limit:
            limit.write(str(dialogueMaxi))

        inLine += 1
        print("fel")
        visualGestore()

while main.RunIterpreter:
	if os.path.exists("script.txt"):
		with open("script.txt","r", encoding="utf-8") as lines:
			for line in lines:
				line = line.replace(" :", ":")
				line = line.replace(":", ": ")
				words=line.split()
				if not line.strip():
					inLine+=1
					continue
				if line.startswith("Character"):
					names.append(words[1])
					print(names)
					if words[2]=="as":
							WorksAsName.append(words[3]+":")
							print(WorksAsName)
							inLine+=1
				elif words[0].rstrip(" ") in WorksAsName:
					speach=" ".join(words[1:])

					for i in variables:
						if "{"+i+"}" in speach:
							print("variable here")
							speach=speach.replace("{"+i+"}",str(variables[i]))
					with open ("dialgue.txt","a",encoding="utf-8")as dilgue:
						dilgue.write(speach+"\n")
					positionToLookAt=WorksAsName.index(words[0])
					nameToWrite=names[positionToLookAt]
					with open ("chractersTurn.txt","a",encoding="utf-8")as ch:
						ch.write(nameToWrite+":\n")
					whichDialogue+=1
					inLine+=1
				if line.startswith("Set"):
					variables[words[1]]={}
					print(variables)
					if words[2]=="to" and not words[3]=="input":
						
						variables[words[1]]=words[3]
					if words[3]=="input":
						print("ansked for input")
						variables[words[1]]=input()
					inLine+=1
				elif words[0] in variables and not words[2] in variables:
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
							print( "you can't reassing a variable to inpùt without an to")
				elif words[0] in variables and words[2] in variables:
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
			seeCharcatersAndText()
			break
	else:
			with open("script.txt","w",encoding="utf-8")as code:
				code.write("Character Erica as e \n ")
				code.write("Character Conan as c \n")
				code.write("e:prueba \n")
				code.write("print hello, world")
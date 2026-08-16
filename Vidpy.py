import clase1
from clase1 import  seeCharcatersAndText
from Visuals import visualGestore
import os
names=[]	
WorksAsName=[]
dialogue=False
OnTest=False
whichDialogue=0
dialogueMaxi=0
toprint=""
visualsCommands=["show","hide"]
#this is for development
if os.path.exists("dialgue.txt") and os.path.exists ("chractersTurn.txt"):
	os.remove("dialgue.txt")
	os.remove("chractersTurn.txt")
if os.path.exists("script.txt" )and OnTest:
	os.remove("script.txt")
text=""
VariablesNames=[]
value=[]
dialogueMaxi = 0

def visuals():
    global words
    global dialogueMaxi

    if words[0] == "show":
        with open("Images And whenToputThem", "a", encoding="utf-8") as iawtt:
            iawtt.write("show " + words[1] + " " + str(whichDialogue) + "\n")

        visualGestore()

    elif words[0] == "hide":
        dialogueMaxi = whichDialogue

        with open("limit" + words[1] + ".txt", "w", encoding="utf-8") as limit:
            limit.write(str(dialogueMaxi))

        print("fel")
        visualGestore()
playing=True
	
while playing:
	if os.path.exists("script.txt"):
		with open("script.txt","r", encoding="utf-8") as lines:
			for line in lines:
				line = line.replace(" :", ":")
				line = line.replace(":", ": ")
				words=line.split()
				if not line.strip():
					continue
				if line.startswith("Character"):
					names.append(words[1])
					print(names)
					if words[2]=="as":
							WorksAsName.append(words[3]+":")
							print(WorksAsName)
				elif words[0].rstrip(" ") in WorksAsName:
					speach=" ".join(words[1:])

					for i in VariablesNames:
						if "{"+i+"}" in speach:
							print("variable here")
							position=VariablesNames.index(i)
							speach=speach.replace("{"+i+"}",str(value[position]))
					with open ("dialgue.txt","a",encoding="utf-8")as dilgue:
						dilgue.write(speach+"\n")
					positionToLookAt=WorksAsName.index(words[0])
					nameToWrite=names[positionToLookAt]
					with open ("chractersTurn.txt","a",encoding="utf-8")as ch:
						ch.write(nameToWrite+":\n")
					print(nameToWrite,":",speach)
					whichDialogue+=1
				if line.startswith("Set"):
					VariablesNames.append(words[1])
					print(VariablesNames)
					if words[2]=="to" and not words[3]=="input":
						
						value.append(words[3])
						print(value)
					if words[3]=="input":
						print("ansked for input")
						value.append(input())
				elif words[0] in VariablesNames and not words[2] in VariablesNames:
						variableToLookThat=VariablesNames.index(words[0])
						if words[1]=="pluss":
							if  True:
								print("hi")
								try:
									firstNumber=int(value[variableToLookThat])
									numberToPluss=int(words[2])
									value[variableToLookThat]=firstNumber+numberToPluss
									toShow=value[variableToLookThat]
									print(toShow)
			
									
								except ValueError:
									print("exception")
				elif words[0] in VariablesNames and words[2] in VariablesNames:
						print("not now")
						variableToLookThat=VariablesNames.index(words[0])
						secondVariable=VariablesNames.index(words[2])
						print(variableToLookThat,secondVariable)
						try:
							number1=int(value[variableToLookThat])
							number2=int(value[secondVariable])
							value[variableToLookThat]=number1+number2
							print(number1+number2)
						except ValueError:
							print("mistake") 
				if words[0] in VariablesNames:
					if words[1]=="to":
						variableToLookThat=VariablesNames.index(words[0])
						if words[2] in VariablesNames:
							print("variable")
						else:
							print("assing"+words[2])
							value[variableToLookThat]=words[2]
				if words[0]=="print":
					toprint=" ".join(words[1:])
					for i in VariablesNames:
						if "{"+i+"}" in toprint:
							variableToLookThat=VariablesNames.index(i)
							toprint=toprint.replace("{"+i+"}",str(value[variableToLookThat]))
					print(toprint)
				elif words[0] in visualsCommands:
					visuals()
			seeCharcatersAndText()
			playing=False
	else:
			with open("script.txt","w",encoding="utf-8")as code:
				code.write("Character Erica as e \n ")
				code.write("Character Conan as c \n")
				code.write("print hello, world")
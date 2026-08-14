import os
names=[]	
WorksAsName=[]
dialogue=False
OnTest=False
toprint=""
#this is for development
if os.path.exists("script.txt" )and OnTest:
	os.remove("script.txt")
text=""
VariablesNames=[]
value=[]
playing=True
while playing:
	if os.path.exists("script.txt"):
		with open("script.txt","r") as lines:
			for line in lines:
				line = line.replace(" :", ":")
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
					with open ("dialgue.txt","a")as dilgue:
						dilgue.write(speach+"\n")
					positionToLookAt=WorksAsName.index(words[0])
					nameToWrite=names[positionToLookAt]
					print(nameToWrite,":",speach)
				elif line.startswith("Set"):
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
			playing=False
	else:
			with open("script.txt","w")as code:
				code.write("Character Erica as e \n ")
				code.write("Character Conan as c \n")
				code.write("e:  hi \n ")
				code.write("Character hattori as h \n")
				code.write("h: not lodabl \n")
				code.write("Set k to input \n")
				code.write("Set x to 2\n")
				code. write("Set other to 20 \n")
				code.write("c:  hi,  I am Conan\n")
				code. write("e: and I am Erica, for {k} time I am not a boy!\n")
				code.write("c: and we have never kill somebody\n")
				code.write("Character MafiaDevs as mf \n")
				code.write("mf: bola sera, bola sera \n")
				code.write("mf: if you just had kept our friendship the ones who did that to your code would have pay it \n")
				code.write("mf: cause the enemies of our friends are our enemies \n")
				code.write("Character me as yo \n")
				code.write("mf: ...  \n")
				
				code.write("yo: I would do anything for you,Alva Majo, the goodfather of game coding \n")
				code.write("other pluss 0 \n")
				code.write("k pluss 5\n")
				code.write("other pluss other \n ")
				code.write("other pluss other \n ")
				code.write("k to 5 \n")
						
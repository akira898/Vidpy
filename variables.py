from refactored import script,inLine
from significant import whichDialogue
import os
operations=["plus","less"]
variables={}
operationsInGame=[]
if os.path.exists("variables.txt"):
    with open("variables.txt","r") as varia:
        for line in varia.read().splitlines():
            lineInVaria=line.split()
            operationsInGame.append(" ".join(lineInVaria[0:]))
        print(operationsInGame)
else:
    print("no variables.txt file found, creating one")
def varia(line):
    global variables
    variables[script[line][1]]={}
    if  script[line][3]  not in variables and  script[line][2]=="to":
        # assign the first variable to a number
        variables[script[line][1]]=script[line][3]
    elif script[line][2]=="to":
        # assign the first variable to the second one
        variables[script[line][1]]=variables[script[line][3]]
    else:
        print("line: ",inLine," you need a to declare a variable")
    print(variables)
def alterVariable(line):
    global operations
    global variables
    if script[line][1] in operations and " ".join(script[line][0:])+" "+str(whichDialogue)not in operationsInGame and len(script[line])==3:
        with open ("variables.txt","a") as varia:
           varia.write(" ".join(script[line][0:])+" "+str(whichDialogue)+"\n")
    else if (script[line][1] in operations and " ".join(script[line][0:])+" "+str(whichDialogue)not in operationsInGame and len(script[line])!=3):
        print("Line: ",inLine," every operation must contain only three ")
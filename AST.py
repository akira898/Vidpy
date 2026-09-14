from refactored import script
from significant import Character,names,WorksAsName,speak,image,toPrint,scenes,jumps
from variables import alterVariable,operations,varia
from clase1 import seeCharcatersAndText
imagesCommands=["show","hide","background"]
for line in script:
    print(script[line])
    if not script[line]:
        continue
    if script[line][0] == "character":
        Character(line)
    elif script[line][0] =="set"and len(script[line])>1:
        varia(line)
    elif script[line][0].rstrip(':') in WorksAsName:
        script[line][0]=script[line][0].replace(":",": ")
        script[line][0]=script[line][0].replace(" :",": ")
        speak(line)
    elif script[line][0] in imagesCommands:
        image(line)
    elif script[line][0]=="print":
        toPrint(line)
    elif script[line][0]=="scene":
        scenes(line)
    elif script[line][0]=="jumps" and len(script[line])>1:
        jumps(line)
    elif len(script[line])>1 and script[line][1] in operations:
        alterVariable(line)
    else:
        print("line: ",line," is not a valid command")
        break
seeCharcatersAndText()

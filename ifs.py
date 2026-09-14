from significant import whichDialogue
from refactored import script
def ifdetec(line):
    with open("ifsInGame.txt","a")as dial:
        dial.write(script[line][1]+" "+script[line][2]+" "+script[line][1]+" "+str(whichDialogue))
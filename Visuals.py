showImage=False
img=""
back=None
place=""
import os
imageSchudele={}
imageSchudele[img] = {}
backgroundSchudele={}
from JumpsAndScenes import ScenesManagment
from main import projectToRun
def visualGestore():
    global showImage
    global img
    global place
    global maxi
    global back
    print("visual time")
    global imageToStart
    global imageSchudele
    with open ("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\Images And whenToputThem.txt", "r", encoding="utf-8") as iawtt:
        for line in iawtt:
            words=line.split()
            showImage=True
            if len(words)<2:
                continue
            print(words)
            if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\Images And whenToputThem.txt"):
                    print(words[1],words[2])
                    img = words[1].replace(".png", "")
            start = int(words[2])

            # Número de instancia
            if len(words) >= 5:
                imper = int(words[4])
                position = words[3]
                if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] +" "+words[4]+".txt"):
                        with open("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] +" "+words[4]+".txt","r",encoding="utf-8") as readingMaximun:
                            maxi=int(readingMaximun.read())
                            img=words[1]
                else:
                    maxi=0
                    print("File not found at ",words[3])
            else:
                imper = int(words[2])
                position = "center"
                print(os.path.exists("limit" + words[1] +" "+ words[2]+".txt"))
                if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] +" "+words[2]+".txt"):
                        with open("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] +" "+words[2]+".txt","r",encoding="utf-8") as readingMaximun:
                            maxi=int(readingMaximun.read())
                            img=words[1]
                else:
                    maxi=200
                    print("File not found")
            if img not in imageSchudele:
                imageSchudele[img] = {}
            # Crear la instancia si no existe
            imageSchudele[img][imper] = {"start": start, "Image to use": img,"position": position,"end": maxi}
            if os.path.exists("backgrounds.txt"):
                        with open("backgrounds.txt","r",encoding="utf-8") as backgrounds:
                            for line in backgrounds:
                                words=line.split()
                                backgroundSchudele[words[1]]={}
                                backgroundSchudele[words[1]]["start"]=int(words[1])
                                if os.path.exists("limit" + words[1] + ".txt"):
                                    with open("limit" + words[1] + ".txt","r",encoding="utf-8") as readingMaximun:
                                        maxi=int(readingMaximun.read())
                       
                                        img=words[1]
                                else:
                                    backgroundSchudele[words[1]]["end"]=200
    showImage=os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem")
    showImage=True
    print(os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem"))
    ScenesManagment()
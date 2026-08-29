showImage=False
img=""
back=None
place=""
import os
imageSchudele={}
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
    with open ("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\Images And whenToputThem.txt", "r", encoding="utf-8") as iawtt:
        for line in iawtt:
            words=line.split()
            showImage=True
            if len(words)<2:
                continue
            print(words)
            if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\Images And whenToputThem.txt"):
                    print(words[1],words[2])
                    img=words[1]
                    img=img.replace(".png","")
                    imageSchudele[img] = {}
                    imageSchudele[img]["start"]=int(words[2])
                    imageSchudele[img]["Image to use"]=img
                    try:
                        imageSchudele[img]["position"]=words[3]
                    except IndexError:
                        imageSchudele[img]["position"]="center"
                    if img=="cuarto":
                        back=True
                    print(os.path.exists("limit" + words[1] + ".txt"))
                    if os.path.exists("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] + ".txt"):
                        with open("projects\\"+projectToRun+"\\Vidpy"+"\\Images"+"\\limit" + words[1] + ".txt","r",encoding="utf-8") as readingMaximun:
                            maxi=int(readingMaximun.read())
                            imageSchudele[words[1]]["end"]=maxi
                            img=words[1]
                

            else:
                print("File not found")
            if os.path.exists("backgrounds.txt"):
                        with open("backgrounds.txt","r",encoding="utf-8") as backgrounds:
                            for line in backgrounds:
                                words=line.split()
                                backgroundSchudele[words[1]]={}
                                backgroundSchudele[words[1]]["start"]=int(words[1])
                                if os.path.exists("limit" + words[1] + ".txt"):
                                    with open("limit" + words[1] + ".txt","r",encoding="utf-8") as readingMaximun:
                                        maxi=int(readingMaximun.read())
                                        backgroundSchudele[words[1]]["end"]=maxi
                                        img=words[1]
                                else:
                                    backgroundSchudele[words[1]]["end"]=200
    showImage=os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem")
    showImage=True
    print(os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem"))
    ScenesManagment()
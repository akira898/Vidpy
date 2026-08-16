showImage=False
img=""
place=""
import os
def visualGestore():
    global showImage
    global img
    global place
    global maxi
    print("visual time")
    with open ("Images And whenToputThem", "r", encoding="utf-8") as iawtt:
        for line in iawtt:
            words=line.split()
            place=int(words[2])

            if words[0]=="show":
                img=words[1]
                print(img)
                img=img.replace(".png","")
    if os.path.exists("limit" + words[1] + ".txt"):
        with open("limit" + words[1] + ".txt","r",encoding="utf-8") as readingMaximun:
          maxi=int(readingMaximun.read())
    showImage=os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem")
    print(os.path.exists("limit" + words[1] + ".txt") and os.path.exists("Images And whenToputThem"))
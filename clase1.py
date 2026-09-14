
import time
import os

# the final version will work with pygame
import pygame
import Visuals
import JumpsAndScenes
from main import projectToRun

# Exponer 'running' para que otros módulos puedan importarl
running = False
numberofImages = 0
test = False
dialogueSeen = []
lines = []
dialogue = 0
pygame.init()


def seeCharcatersAndText():
    global running
    global dialogue
    clicks = 0
    with open("projects\\"+projectToRun+"\\Vidpy"+"\\dialgue.txt", "a", encoding="utf-8") as speach:
        speach.write("")
    with open("projects\\"+projectToRun+"\\Vidpy"+"\\chractersTurn.txt", "a", encoding="utf-8") as characters:
        characters.write("")
    global numberofImages

    with open("projects\\"+projectToRun+"\\Vidpy"+"\\dialgue.txt", "r", encoding="utf-8") as speach:
        global lines
        for line in speach:
            lines.append(line.rstrip("\n\r"))
    with open("projects\\"+projectToRun+"\\Vidpy"+"\\chractersTurn.txt", "r", encoding="utf-8") as characters:
        names = []
        for line in characters:
            names.append(line.rstrip("\n\r"))

    screen = pygame.display.set_mode((720,600))
    pygame.display.set_caption("Speaker")
    running = True
    textToShow=[]
    clock=clock = pygame.time.Clock()
    def rload(screen):
        global dialogue
        global text
        global lines
        global textCharacter
        print(JumpsAndScenes.sceneData)
    rload(screen)
    font = pygame.font.Font(None, 25)
    characterIn=0
    lastCharacterT= pygame.time.get_ticks()
    while dialogue < len(lines) and running:
        screen.fill((0, 0, 0))
        textToShow=[]
        currentT=pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("I gave you the world you threw it away")
                    print(dialogue)
                    dialogueSeen.append(dialogue)
                    textToShow=[]
                    dialogue += 1
                    for name, scene in JumpsAndScenes.sceneData.items():
                        print(name)
                        if scene.jump == dialogue:
                            dialogue = scene.line
                            break
                    characterIn=0
                    clicks += 1
                    rload(screen)
            elif event.type==pygame.FINGERDOWN:
                    print("I gave you the world you threw it away")
                    print(dialogue)
                    dialogueSeen.append(dialogue)
                    textToShow=[]
                    dialogue += 1
                    for name, scene in JumpsAndScenes.sceneData.items():
                        print(name)
                        if scene.jump == dialogue:
                            dialogue = scene.line
                            break
                    characterIn=0
                    clicks += 1
                    rload(screen)
        if Visuals.showImage:
            backgorundPath=os.path.join("projects", projectToRun, "images","cuarto.png")
            # this the same thing of the images but with the background
            #and why isn't working
            #fuck this
            for name,item in Visuals.backgroundSchudele.items():
                if item["start"] <= dialogue and item["end"] > dialogue:
                    print(name)
                    imageToLook = os.path.join("projects", projectToRun, "images",name + ".png")
                    print(imageToLook)
                    if os.path.exists(imageToLook):
                        background = pygame.image.load(imageToLook).convert_alpha()
                        screen.blit(background, (0, 0))
                    else:
                        print("doesn't")
            # this tracks the image and makes sure its there when needed
            for name,instances in Visuals.imageSchudele.items():
                for instance, item in instances.items():
                    if item["start"] <= dialogue < item["end"]:
                        imageToLook = os.path.join("projects",projectToRun,"images",name + ".png")
                        if not os.path.exists(imageToLook):
                            imageToLook = os.path.join("projects",projectToRun,"images", name + ".JPG")
                        if os.path.exists(imageToLook):
                            image = pygame.image.load(imageToLook).convert_alpha()
                            if item["position"] == "left":
                                screen.blit(image, (100, 100))
                            elif item["position"] == "right":
                                screen.blit(image, (500, 100))
                            else:
                                screen.blit(image, (300, 100))
        if  dialogue < len(lines):
            if characterIn<  len(lines[dialogue]) and currentT-lastCharacterT>=50:
                characterIn+=1
                lastCharacterT=currentT
            text = font.render(lines[dialogue][:characterIn], True, (255, 255, 255))
            textCharacter = font.render(names[dialogue], True, (255, 255, 255))
            screen.blit(text, (100, 540))
            screen.blit(textCharacter, (100, 520))
        # time.sleep(0.5)
        pygame.display.flip()
        clock.tick(60)

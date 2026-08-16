from email.mime import image
import os
# the final version will work with pygame
import pygame
import Visuals 
# Exponer 'running' para que otros módulos puedan importarl
running = False
numberofImages=0
test=False
pygame.init()
def seeCharcatersAndText():
    global numberofImages
    with open("dialgue.txt", "r", encoding="utf-8") as speach:
        global lines
        lines = speach.readlines()
    with open("chractersTurn.txt", "r", encoding="utf-8") as characters:
        names = characters.readlines()
    print(lines)
    dialogue=0
    if test==True:
        import tkinter as tkin
        ventana=tkin.Tk()
        ventana.title("Vidpy")
        advance=tkin.Button(ventana,text="Advance",command=adva)
        advance.pack()
        ventana.mainloop()
    else:
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("text")
        pygame.display.set_caption("Speaker")
        font=pygame.font.Font(None,20)
        running=True
        while dialogue<len(lines) and running:
            screen.fill((0, 0, 0))
            if Visuals.showImage:
                if dialogue<Visuals.maxi and dialogue>=Visuals.place :

                  image=pygame.image.load(Visuals.img+".png")
                  if numberofImages==0:
                      screen.blit(image,(0,0))
                      numberofImages+=1
                  else:

                      screen.blit(image,(100,0))
                else:
                    screen.fill((0, 0, 0))
            else:
                screen.fill((0, 0, 0))
            text = font.render(lines[dialogue], True, (255, 255, 255))
            # this is just a test
            textCharacter = font.render(names[dialogue], True, (255, 255, 255))
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        dialogue += 1
            screen.blit(text,(100,100))
            screen.blit(textCharacter,(100,80))
            pygame.display.flip()



    def adva():
      nonlocal dialogue
      dialogue+=1
      print(names[dialogue])
      print(lines[dialogue])

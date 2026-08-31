import os
import time
from main import projectToRun
eraseComplete=False
def restart():
    global eraseComplete
    carpet=os.path.join("projects"+projectToRun+"\\Vidpy"+"\\jumps")

    for filename in os.listdir(carpet):
        file_path = os.path.join(carpet, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)
    ImagesInfo=os.path.join("projects",projectToRun,"Vidpy","Images")
    if os.path.exists(ImagesInfo):
        for filename in os.listdir(ImagesInfo):
            file_path = os.path.join(ImagesInfo, filename)
            time.sleep(5)
            print(filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        time.sleep(5)
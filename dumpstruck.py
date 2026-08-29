import os
from main import projectToRun
eraseComplete=False
def restart():
    global eraseComplete
    carpet=os.path.join("projects"+projectToRun+"\\Vidpy"+"\\jumps")

    for filename in os.listdir(carpet):
        file_path = os.path.join(carpet, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)
    eraseComplete=True
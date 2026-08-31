
projects=[]
import os
projectsCarpets={}
textAppear=True
RunIterpreter=False
if not os.path.exists("projects"):
    os.makedirs("projects", exist_ok=True)
if  os.path.exists("projects.txt"):
    with open("projects.txt","r",encoding="utf-8") as projectsInMemory:
        for line in projectsInMemory:
            ProjectToCheck = line.rstrip("\n\r")
            projects.append(ProjectToCheck)
            print(projects)
while not RunIterpreter:
    if textAppear:
        print("Welcome to the alpha of vidpy, a visual novel engine dshined for phones and computers")
        print("This aplha doesn't have: branching,arimatic")
    print ("write run + the name of a project to run it, write create+ name of the project to create it")
    textAppear=False
    command=input("Enter command:")
    words=command.split()
    if command.startswith("run "):
        try:
            projectToRun=" ".join(words[1:])
            if projectToRun in projects:
                RunIterpreter=True
        except IndexError:
            print("You must write the name of the project")
    elif words[0]=="create": 
        try:
            name=" ".join(words[1:])
            projects.append(name)
            location="projects\\"+name
            os.makedirs(location)
            imagesLocation=location+"\\images"
            os.makedirs(imagesLocation)
            gestionFiles=location+"\\Vidpy"
            os.makedirs(gestionFiles)
            gestionFilesjump=gestionFiles+"\\jumps"
            os.makedirs(gestionFilesjump)
            gestionFilesImages=gestionFiles+"\\Images"
            os.makedirs(gestionFiles+"\\Images")
            with open (location+"\\script.txt","w",encoding="utf-8") as code:
                code.write("Character Erica as e\n")
                code.write("e:Hello world\n")
                code.write("e:This is a test\n")
            print("Project created, now you can write your VN with the archive",location+"\\script.txt and ",imagesLocation," carpet to put your images")
            with open("projects.txt","a") as projects:
                projects.write(name+"\n")

        except IndexError:
            print("For creating a project you need to write the name of it")
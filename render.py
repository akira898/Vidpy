import os
while True:
    if os.path.exists("dialgue.txt"):
        with open("dialgue.txt","r") as speach:
            line=speach.read()
        print(line)
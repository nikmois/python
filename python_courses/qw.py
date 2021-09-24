numbers = 0
with open("numbse.txt", "r") as file:
    r = file.read()
    lines = r.splitlines()
    for i in lines:
        numbers = i.split(",")

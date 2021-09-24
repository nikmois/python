with open("frt.csv", "r") as file:
    text = file.read()

wer = []
words = text.split(' ')
print(words)

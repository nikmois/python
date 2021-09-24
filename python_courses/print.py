import re
hand = open('text.txt')
numlist = list()
count = 0

for line in hand:
    line = line.rstrip()
    numlist = re.findall('[0-9]+', line)
    inp = list(numlist)
    if numlist == []:
        continue
    for yy in numlist:
        count = count + int(yy)
print(count)

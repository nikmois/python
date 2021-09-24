import re
fname=input('Whats up?')
fh=open(fname, 'r')
y=list()
count=0

for line in fh:
    y=re.findall('[0-9]+', line)
    inp=list(y)
    if y == []:
        continue
    count=count+int(y[0])
print(count)

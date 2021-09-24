fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        x = line.split()
        re = x[1]
        counts[re] = counts.get(re,0) + 1

bigcount = None
bigword = None
for re,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = re
        bigcount = count

print(bigword, bigcount)

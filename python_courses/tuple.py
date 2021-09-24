fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        x = line.split()
        re = x[5]
        ner = re.split(':')
        we = ner[0]
        counts[we] = counts.get(we,0) + 1
lst = list()
for key, val in counts.items():
    ter = (key, val)
    lst.append(ter)

lst = sorted(lst)
for key, val in lst:
    print(key, val)

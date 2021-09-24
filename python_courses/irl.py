fname = input('Enter fail name: ')
fail = open(fname)
for a in fail:
    ler = a.split()
ner = ler.sort()
print(ner)

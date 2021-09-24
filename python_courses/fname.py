fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    xe = line.rstrip()
    print(xe.upper())

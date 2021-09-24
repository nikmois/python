fname = input('Enter file name: ')
fh = open(fname)
count = 0
lines = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        lines = lines + 1
        xe = line.find(" ")
        er = line[xe:]
        xs = er.lstrip()
        x = float(xs)
        count = count + x
        continue
print('Average spam confidence:',count/lines)

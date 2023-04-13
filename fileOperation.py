f = open('myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline, end = '')
print(secondline)

f.close()

f = open('myfile.txt', 'a')

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')

f.close()

f = open('myfile.txt', 'r')
for line in f:
    print(line, end = '')

f.close()

#  Writing to a Text File

""" print('opening file')
f = open('l9_filen.txt', mode = 'a')
f.write('First file\n')
f.write('\nSecond line\n')
f.close()
print('file closed') """

""" print('opening file')
f = open('l9_filen.txt', mode = 'r')
line = f.read()
print(line)
print('file closed') """

#print('opening file')
""" f = open('l9_filen.txt', mode = 'r')

for i in range(0,3):
    line = f.readline()
    print(line)
#    print('file closed')
f.close() """

""" f = open('L9_filen.txt', mode = 'r')
fw= open('L9_filen_caps.txt', mode = 'w')
f_read = f.read()
fw.write(f_read.upper())
f.close() """

f = open('L9_filen.txt', mode = 'r')
fw= open('L9_filen_caps.txt', mode = 'w')
fw.write(f.read().upper())
f.close()
fw.close()
         
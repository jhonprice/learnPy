poem='''\
asdasdadad
adasdad
asdadad
'''

f = open(r'D:\out.txt','w')

f.write(poem)

f.close()

f = open(r'D:\out.txt','r')
while True:
    line = f.readline()

    if len(line) == 0:
        break

    print(line,end='')

f.close()

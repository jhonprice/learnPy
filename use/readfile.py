f = open(r'D:\B\learnPy\use\location.txt','r',encoding='UTF-8')

m = {}

while True:
    line = f.readline().rstrip("\n")
    if len(line) == 0:
        break
    ls = line.split("=")
    m[ls[1]]=ls[0]

f.close()


f2 = open(r'D:\B\learnPy\use\filter.txt','r',encoding='UTF-8')

flist = f2.read().splitlines()


for k in flist:
    print("\""+m[k]+"\"",end=',')

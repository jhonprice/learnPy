rf = open(r'D:\B\learnPy\use\android.txt','r',encoding='UTF-8')

m={}

while True:
    line = rf.readline().rstrip("\n")
    if len(line) == 0:
        break
    ls = line.split(",")
    m[ls[1]]=ls[2]

rf.close()


rf = open(r'D:\B\learnPy\use\qqqq.txt','r',encoding='UTF-8')

mm={}

while True:
    line = rf.readline().rstrip("\n")
    if len(line) == 0:
        break
    ls = line.split(";")
    mm[ls[0]]=ls[1]

rf.close()


rA={}

for k,v in m.items():
    rA[mm[k]]=v




rf = open(r'D:\B\learnPy\use\location.txt','r',encoding='UTF-8')

mmm={}

while True:
    line = rf.readline().rstrip("\n")
    if len(line) == 0:
        break
    ls = line.split("=")
    mmm[ls[0]]=ls[1]

rf.close()


rmap ={}

for k,v in rA.items():
    rmap[mmm[k]]=v


for k,v in rmap.items():
    print(k,v,sep=':')


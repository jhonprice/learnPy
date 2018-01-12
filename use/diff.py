f = open(r'D:\B\doc\运营支持\eq','r')

l = f.read().splitlines()


f.close()


f = open(r'D:\B\doc\运营支持\qe.csv','r')

ll = f.read().splitlines()

f.close()

m={}
for item in l:
    if item in m.keys():
        m[item]+=1
    else:
        m[item]=0

print(m)
#for item in ll:
#    if item not in l:
#        print(item)

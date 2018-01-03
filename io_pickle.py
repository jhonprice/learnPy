import pickle

fileName = r'D:\d.data'

l = ['A','B','C']


f = open(fileName,'wb')

pickle.dump(l,f)
f.close()


del l

f = open(fileName,'rb')

ll = pickle.load(f)

print(ll)

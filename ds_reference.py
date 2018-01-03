list1 = ['1']

list2 = ['2']


mlist1 = list1
mlist2 = list2.copy()



print("before",mlist1)
list1.append('3')
print("after",mlist1)

print("before",mlist2)
list2.append('4')
print('after',mlist2)

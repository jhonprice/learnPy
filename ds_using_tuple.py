zoo = ('A','B','C')

print('Number of zoo is',len(zoo))
new_zoo = 'monkey','camel',zoo


print('Len',len(new_zoo))
print('New',new_zoo)
print('Old Tuple',new_zoo[2])
print('Item In Old Tuple',new_zoo[2][2])
print('New Len',len(new_zoo)-1+len(new_zoo[2]))

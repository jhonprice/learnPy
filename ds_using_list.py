shoplist=['A','B','C','D']

print("len(shoplist)",len(shoplist))

print('show',end=' ')

for item in shoplist:
    print(item,end=' ')

print()

print("append")

shoplist.append("E")

print('list is',shoplist)

print('first item',shoplist[0])

olditem = shoplist[0]

del shoplist[0]

print('delete',olditem)

print('list is',shoplist)

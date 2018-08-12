def person(name,age,**kw):
    print('name',name,'age',age,'other:',kw)

print('''
def person(name,age,**kw):
    print('name',name,'age',age,'other:',kw)
''')

print("person('M',30)",person('M',30),sep="\n")


extra = {'city':'Beijing','job':'Engineer'}

print("person('J',24,**extra)",person('J',24,**extra))



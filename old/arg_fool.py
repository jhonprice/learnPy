def add_end(L=[]):
    L.append("fool")
    return L


def add_endd(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print('''def add_end(L=[]):
    L.append("fool")
    return L''')

print("add_end()",add_end())
print("add_end()",add_end())



print('''
def add_endd(L=None):
    if L is None:
        L = []
    L.append("END")
    return L
''')

print("add_endd()",add_endd())
print("add_endd()",add_endd())


ab = {
    'A':'a',
    'B':'b',
    'C':'c',
    'D':'d',
    'E':'e'
}


print("A is",ab['A'])


del ab['E']

print("len {0}".format(len(ab)))

for k,v in ab.items():
    print("k{0},v{1}".format(k,v))

ab['E'] = 'e'

if 'E' in ab:
    print('E is',ab['E'])

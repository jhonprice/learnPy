print ('''def calc(*numbers):
    sum = 0
    for n in numbers:
        sum +=(n*n)
    return sum
''')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum +=(n*n)
    return sum

print("calc(1,2)",calc(1,2))

nums = [1,2,3]

print("calc(*nums)",calc(*nums))


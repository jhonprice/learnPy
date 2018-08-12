g = (x * x for x in range(12))

print("next(g)",next(g))
print("next(g)",next(g))

for n in g:
    print(n)


def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n = n+1
    return 'done'


f = fib(6)

print("fib generator:",f)

for n in f:
    print(n)


g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

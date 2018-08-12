x = 50
y = 10

def func():
    global x,y

    print('x is',x)
    print('y is',y)
    x = 2
    y = 1
    print('Changed global x y to',x,y)

func()
print('value of x is',x,y)

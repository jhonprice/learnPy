#文档字符串第一行大写字母开头,以句号结束,
#第二行空行
#第三行详细说明

def print_max(x,y):
    '''Prints max
    two int'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')


print_max(3,5)
print(print_max.__doc__)

#使用命名关键字参数时，要特别注意，如果没有可变参数，
#就必须加一个*作为特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

print('''
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
''')

person('a','b','c','d',city='e',job='f')



#对于任意函数，都可以通过类似func(*args, **kw)的形式调用
def f1(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)
    return ""

args=(1,2,3)
kw={'d':99,'x':'#'}


print('''
def f1(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)

args=(1,2,3)
kw={'d':99,'x':'#'}
''')

print("f1(*args,**kw)"+f1(*args,**kw))


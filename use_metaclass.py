class ListMetaclass(type):
    #准备创建的类的对象,类名,父类集合,方法集合
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass


L1 = MyList()
L1.add(1)

print(L1)

L2 = list()
L2.add(1)




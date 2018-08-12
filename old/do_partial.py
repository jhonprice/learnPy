import functools

int2 = functools.partial(int,base=2)


print('1000000000 = ',int2('1000000000'))

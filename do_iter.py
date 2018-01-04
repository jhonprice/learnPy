from collections import Iterable,Iterator

print("isinstance([],Iterator)",isinstance([],Iterator))
print("isinstance([],Iterable)",isinstance([],Iterable))
print("isinstance(iter([]))",isinstance(iter([1,2,3]),Iterator))

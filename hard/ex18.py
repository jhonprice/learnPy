#函数与参数

#this one is like your scripts with argv
def print_two(*args):
    a,b=args;
    print(f"arg1: {a},arg2:{b}")

def print_two_again(a,b):
    print(f"arg1: {a},arg2:{b}")


def print_one(a):
    print(f"arg1: {a}")


def print_none():
    print("I got nothing")


print_two("aaa","bbb")
print_two_again("ccc","ddd")
print_one("eee")
print_none()

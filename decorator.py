import functools

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper




def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


@log("adsad")
def now():
    print('a')

now()

print(now.__name__)

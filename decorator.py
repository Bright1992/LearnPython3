import functools

def decorator(text):
    def log(func):
        print("log")        #Executed when decleared
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("call: %s"%func.__name__)     #Executed when called
            ret = func(*args,**kw)
            print("call end: %s"%func.__name__)
            return ret
        return wrapper
    return log

@decorator('test')
def foo(text):
    print(text)
    return 1

if __name__=='__main__':
    print(foo.__name__)
    print(foo('foo1') )
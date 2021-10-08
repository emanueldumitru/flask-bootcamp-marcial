# higher order functions - function that accept another functions

def greet(func):
    x = func()
    print(x)

    
def greet2():
    def functie():
        return 5
    return functie

#decorator add extra feature to functions 

def hello():
    print('hellooooo')
    
def my_decorator(func): #*args, **kwargs
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func

@my_decorator
def hello():
    print('hellooooo')
    
@my_decorator
def bye():
    print('see ya later')
    
    
# another decorator example 

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper    

@performance
def long_time():
    for i in range(100000000):
        i * 5

def main(): 
    greet(greet2())
    hello()
    bye()

    #how does decorator works under the hood 
    hello2 = my_decorator(hello)
    hello2()
    
    long_time()

if __name__ == '__main__':
    main()
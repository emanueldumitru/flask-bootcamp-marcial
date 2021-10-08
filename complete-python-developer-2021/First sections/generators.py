from decorators import performance

@performance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5
        
@performance
def long_time2():
    print('2')
    for i in range(10000000):
        yield i * 5

long_time()
long_time2()

# generators under the hood 
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break
        
special_for([1,2,3])

# my own generator - range 
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
    
        
gen = MyGen(0, 100)
for i in gen:
    print(i)

def generator_function(num): #iterable
    for i in range(num):
        yield i * 2 #give i and pause the function

g = generator_function(100)
next(g)
next(g)
print(next(g))

# for item in generator_function(1000):
    # print(item)
    
# def make_list(num):
    # result = []
    
    
def fib(number):
    a = 0
    b = 1 
    for i in range(number):
        yield a
        temp = a
        a = b 
        b = temp + b
for x in fib(20):
    print(x)
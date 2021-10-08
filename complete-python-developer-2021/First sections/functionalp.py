#pure function - just a function f : input -> output,


# map, filter, zip and reduce
my_list = [1,2,3]
your_list = (10, 20, 30)
their_list = (5, 4, 3)
def multiply_by2(item):
    return item * 2

def check_odd(item):
    return item % 2 != 0

from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item   

# lambda expressions, anonymous functions  
my_list = [5,4,3]
new_list = list(map(lambda num: num **2, my_list))
print(new_list)

a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key=lambda x : x[1])
print(a)

# comprehension
print([num**2 for num in range(0,100) if num % 2 == 0])
print({num for num in range(0,100)})

simple_dict = {
    'a' : 1,
    'b' : 2,
}
print({key:value**2 for key,value in simple_dict.items() if value % 2 == 0})


def main():
    print(list(map(multiply_by2, my_list)))
    print(list(filter(check_odd, my_list)))
    print(list(zip(my_list, your_list, their_list)))
    print(reduce(accumulator, my_list, 0))
    
    print(list(map(lambda item: item * 3, my_list)))
    print(reduce(lambda acc, item: acc + item, my_list))

if __name__ == '__main__':
    main()
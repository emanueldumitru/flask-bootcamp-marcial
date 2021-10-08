# Data types .. how to manipulate data
# int, float, bool, str, list, tuple, set, dict
# classes - custom types
# specialized data types - modules, extensions to the language
# None type
# bin


def main():
    """[summary]
       This is the maid function 
    """
    x = 123
    print("Welcome to python")

    name = "Emanuel"
    age = 27
    print(f"Hi {name}, you are {age} years old")

    # is also check in memory allocation
    # enumerate index

    # Walrus operator
    a = 'helllloooooo'
    if ((n := len(a)) > 10):
        print(f"too long {n} elements")

    outer()


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)
    inner()
    print("outer: ", x)


def lists_topic():
    #slicing and methods
    # list unpacking
    a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7]
    pass


def dict_topic():
    # dict topic, also tuples can be used as keys
    pass


def tuples_topic():
    pass


def set_topic():
    pass


if __name__ == '__main__':
    main()

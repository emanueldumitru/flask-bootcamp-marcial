# Error handling 

def sum(num1, num2):
    try:
        return num1/num2
    except (ZeroDivisionError, ValueError) as err:
        print(err)
    except TypeError as err:
        print('please enter number ' + err)
        
print(sum(1,1))

while True:
    try:
        age = int(input('what is your age: '))
        10/age
        raise ValueError('hey cut it out')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break 
    finally:
        print('ok, im am finally done')
    
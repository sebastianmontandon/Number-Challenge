"""
Challenge 1:
    Make a function that receive as parameter an int, and return true or false if this int its a prime number
"""

def is_prime(number:int):
    if number == 1:
        return False
    for prev_number in range(2, number):
        if number % prev_number == 0:
            return False
    return True

"""
Challenge 2:
    Make a function that receive as parameter an int, and return factorial result
"""

def calulate_factorial(number:int):
    for i in range(1, number):
        number = number * i
    return number or 1

"""
Challenge 3:
    Make a function that receive as parameter an int, and return the result of sum all points of the triangle like this,
        *
        **
        ***
        ****
        ***** = 15
"""

def triangle_number(number:int):
    if number == 0:
        return 0
    return number + triangle_number(number - 1)


# print(triangle_number(6))

# print(calulate_factorial(5))

# print(is_prime(43))


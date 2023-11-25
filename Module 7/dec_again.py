import math
def timer(fun):
    def inner(*args, **kargs):
        print('time started')
        #print(fun)
        fun(*args, **kargs)
        print('time ended')
    return inner

#timer()()
@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'the factorial of {n} is {result}')

#timer(get_factorial)() # this also works like a decorator

get_factorial(1500)

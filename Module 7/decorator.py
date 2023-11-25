def timer(fun):
    def inner():
        print('time started')
        #print(fun)
        fun()
        print('time ended')
    return inner

#timer()()
@timer
def get_factorial():
    print('factorial starting')

#timer(get_factorial)() # this also works like a decorator

get_factorial()
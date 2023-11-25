def outer_fun():
    print('printing outer stuff')

    def inner_fun():
        print("its inner fun")
    return inner_fun

print(outer_fun()())

def do_something(work):
    print('opeing do someting')
    print('do someting ending')
    work()


def coding():
    print('coding in python')


do_something(coding)
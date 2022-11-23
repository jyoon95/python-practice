def arb_args(*args):
    for i in args:
        print(args)

def inner_func(x, y):
    def inner_1():
        return x + y
    def inner_2():
        return x - y
    print(inner_1() + inner_2())

def lunch_lady(name, lunch = 'mystery meat'):
    print(name, lunch)
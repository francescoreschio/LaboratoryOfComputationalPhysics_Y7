def my_dec(func):
    def wrapper(x):
        print('Hello!')
        return func(x)
    return wrapper
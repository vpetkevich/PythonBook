def test(func):
    def func_description(*args):
        print('start')
        result = func(*args)
        print('end')
        return result
    return func_description


@test
def sum_all(a, b):
    return a + b

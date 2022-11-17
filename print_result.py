# Здесь должна быть реализация декоратора

def print_result(func):
    def wrapper_func(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if type(res) is list:
            for el in res:
                print(el)
        elif type(res) is dict:
            d_keys = list(dict(res).keys())
            for k in d_keys:
                print(str(k) + ' = ' + str(res[k]))
        else:
            print(res)
        return res

    return wrapper_func


@print_result
def test_1():
    return


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

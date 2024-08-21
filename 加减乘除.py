def add(*args):
    return sum(args)


def minus(a, *args):
    return a - sum(args)



def multiply(*args):
    return 1 if not args else args[0] * multiply(*args[1:])


def divide(a, *args):
    if not args:
        return a
    divisor = 1
    for arg in args:
        if arg == 0:
            raise ValueError("Cannot divide by zero")
        divisor *= arg
    return a / divisor


def cal(fun, *args):
    operations = {
        'add': add,
        'minus': minus,
        'multiply': multiply,
        'divide': divide
    }
    if fun in operations:
        return operations[fun](*args)
    else:
        raise ValueError(f"Unsupported operation: {fun}")

    # 测试函数


print(cal('add',1,2,3))
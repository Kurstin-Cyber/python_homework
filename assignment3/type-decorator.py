def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result =  func(*args, **kwargs)
            return type_of_output(result)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

if __name__ == '__main__':
    y = return_int()
    print(f'Result of return_int (now {type(y).__name__}): {y}')

    try:
        y = return_string()
        print(f'Result of return_int (now{type(y).__name__}: {y})')
    
    except ValueError:
        print("Can't convert that string to an interger.")
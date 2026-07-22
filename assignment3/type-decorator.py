def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return type_of_output(result)
            except (ValueError, TypeError) as e:
                
                print(f'Error converting type: {e}')
                return None
        return wrapper
    return decorator
    
    


@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

if __name__ == '__main__':
    y = return_int("42")
    print(type(y).__name__)

    try:
        y =return_string()
        print("shouldn't get here!")
    except ValueError:
        print("Can't convert that string to an integer!")
    
    
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
    
    


@type_converter(int)
def convert_value(val):
    return val


if __name__ == '__main__':
    y = convert_value("42")
    if y is not None:
        print(type(y).__name__)
    
    convert_value("not_an_integer")
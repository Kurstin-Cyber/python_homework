import logging 

logger = logging.getLogger(__name__ + '_parameter_log')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('./decorator.log', 'a')
logger.addHandler(handler)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_params = list(args) if args else 'none'
        kw_params = kwargs if kwargs else 'none'

        result = func(*args, **kwargs)

        log_entry = (
            f'\nfunction: {func.__name__}\n'
            f'positional parameters: {pos_params}\n'
            f'keyword parameters: {kw_params}\n'
            f'return: {result}'
        )

        logger.log(logging.INFO, log_entry)
        return result
    return wrapper

@logger_decorator
def greet():
    print('Hello, World!')

@logger_decorator
def p_args(*args):
    return True


@logger_decorator
def get_decorator_info(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    greet()
    p_args(10, 20, 30)
    get_decorator_info(test_key='test_value')


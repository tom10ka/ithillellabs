def string_refactor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is str:
            result = f'<b>{result}</b>'
        return result

    return wrapper

def save_result(filename, pen):
    path = './images/' + filename

    def inner(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            nonlocal path
            path = path.format_map(kwargs)
            pen.getcanvas().postscript(file=path)
        return wrapper
    return inner

def save_canvas(filename, pen):
    path = './images/' + filename

    def inner(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            nonlocal path
            path = path.format_map(kwargs)
            pen.getcanvas().postscript(file=path)
            print('Speichern des Bildes abgeschlossen.')
        return wrapper
    return inner

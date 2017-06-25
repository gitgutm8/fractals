def save_canvas(filepath, pen):
    path = './images/' + filepath + '.eps'

    def inner(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            nonlocal path
            path = path.format_map(kwargs)
            pen.getcanvas().postscript(file=path)
            print(f'Speichern des Bildes in {path} abgeschlossen.')
        return wrapper
    return inner

import turtle


def _fractal_triangles(side_length, depth):
    if depth <= 0:
        return
    half_side_length = side_length / 2
    for _ in range(3):
        turtle.forward(half_side_length)
        turtle.left(120)
        turtle.forward(half_side_length)
        turtle.left(180)
        _fractal_triangles(side_length / 3, depth=depth-1)
        turtle.left(180)


def fractal_triangles(first_side_length, depth=5, **kwargs):
    turtle.pen(**kwargs)
    turtle.begin_fill()
    _fractal_triangles(first_side_length, depth)
    turtle.end_fill()


if __name__ == '__main__':
    fractal_triangles(400, depth=4,  speed=0, fillcolor='red', shown=False)
    turtle.done()
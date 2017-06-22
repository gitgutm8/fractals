import turtle


def _draw_koch(length, depth):
    if depth <= 0:
        turtle.forward(length)
    else:
        length /= 3
        depth -= 1
        # Ausrichtung: 60° -> 300° -> 0° -> 0°
        for rotation in (60, 240, 60, 0):
            _draw_koch(length, depth)
            turtle.left(rotation)


def _draw_snowflake(length, depth):
    for _ in range(3):
        _draw_koch(length, depth)
        turtle.right(120)


def draw_snowflake(length, depth=4, **kwargs):
    turtle.pen(**kwargs)
    _draw_snowflake(length, depth)
    turtle.done()


if __name__ == '__main__':
    draw_snowflake(300, depth=5, shown=False, speed=0)

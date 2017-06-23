import turtle
import os
from save_result import save_canvas


def _draw_koch(length, depth):
    """https://de.wikipedia.org/wiki/Koch-Kurve#Konstruktion"""
    if depth <= 0:
        turtle.forward(length)
    else:
        length /= 3
        depth -= 1
        # Ausrichtung: 60° -> 300° -> 0° -> 0°
        for rotation in (60, 240, 60, 0):
            _draw_koch(length, depth)
            turtle.left(rotation)


def _center_snowflake(length):
    turtle.penup()
    turtle.left(180)
    turtle.forward(length / 2)
    turtle.right(90)
    height = 3**0.5 * 0.5 * length
    turtle.forward(height / 2)
    turtle.right(90)
    turtle.pendown()


def _draw_snowflake(length, depth):
    _center_snowflake(length)
    for _ in range(3):
        _draw_koch(length, depth)
        turtle.right(120)


@save_canvas('snowflakes/koch_snowflake_{depth}', turtle)
def draw_snowflake(length, depth=4, **kwargs):
    turtle.pen(**kwargs)
    _draw_snowflake(length, depth)


if __name__ == '__main__':
    if not os.path.exists('./images/snowflakes'):
        os.mkdir('./images/snowflakes')
    draw_snowflake(300, depth=3, shown=False, speed=0)
    turtle.done()

"""
L-System der Drachenkurve:

Winkel: 90°
Konstanten: F + -
Variablen: X Y
Anfangsstück: FX
Ableitungsregeln:
    X -> X + Y F +
    Y -> - F X - Y

F: Strecke nach vorne
+: Gegen den Urzeigersinn (left)
-: Im Urzeigersinn (right)
"""

import turtle
import os
from save_result import save_canvas


def draw_X(length, depth):
    if depth <= 0:
        return
    draw_X(length, depth-1)
    turtle.left(90)
    draw_Y(length, depth-1)
    turtle.forward(length)
    turtle.left(90)


def draw_Y(length, depth):
    if depth <= 0:
        return
    turtle.right(90)
    turtle.forward(length)
    draw_X(length, depth-1)
    turtle.right(90)
    draw_Y(length, depth-1)


@save_canvas('dragon/dragoncurve_{depth}', turtle)
def draw_dragon(length, depth=5, **kwargs):
    turtle.pen(**kwargs)
    turtle.setheading(90)
    turtle.forward(length)
    draw_X(length, depth)


if __name__ == '__main__':
    if not os.path.exists('./images/dragon'):
        os.mkdir('./images/dragon')
    draw_dragon(1, depth=15, shown=False, speed=0)
    turtle.done()

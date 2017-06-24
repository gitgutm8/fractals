"""
L-System des Binärbaums

Variablen: F X
Konstanten: [ ]
Axiom: F
Regeln:
    F -> X [ F ] F
    X -> X X

[ Pos und Winkel speichern, 45° links
] Pos und Winkel abrufen, 45° rechts
"""

import turtle
from save_result import save_canvas
import os


def _draw_F(length, depth, stack):
    if depth <= 1:
        turtle.forward(length)
        return
    _draw_X(length, depth-1)
    stack.append((turtle.position(), turtle.heading()))
    turtle.left(45)
    _draw_F(length, depth-1, stack)
    pos, dir = stack.pop()
    turtle.penup()
    turtle.setposition(pos)
    turtle.setheading(dir)
    turtle.pendown()
    turtle.right(45)
    _draw_F(length, depth-1, stack)


def _draw_X(length, depth):
    if depth <= 1:
        turtle.forward(length)
        return
    for _ in range(2):
        _draw_X(length, depth-1)


@save_canvas('trees/tree_{pencolor}_{depth}', turtle)
def draw_tree(length, depth=5, **kwargs):
    turtle.pen(**kwargs)
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(turtle.xcor(), -turtle.screensize()[1])
    turtle.pendown()
    _draw_F(length, depth, [])


if __name__ == '__main__':
    if not os.path.exists('./images/trees'):
        os.mkdir('./images/trees')

    draw_tree(0.1, depth=13, speed=0, shown=False, pencolor='green')
    turtle.done()

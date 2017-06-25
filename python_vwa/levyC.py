"""
L-System der Lévy-C-Kurve

Winkel: 45°
Konstanten: F + -
Variablen: [x]
Ableitungsregeln:
    F -> - F + + F -
"""

import turtle
from save_result import save_canvas
import os
import itertools


COLORS = itertools.cycle(['red', 'orange', 'yellow', 'green', 'blue4', 'blue', 'purple'])


def rainbow(counter):
    if counter % 10 == 0:
        turtle.pencolor(next(COLORS))


def draw_F(length, depth, counter=0):
    """
    Zeichnet rekursiv Streckenabschnitte.
    :param length: Länge des Streckenabschnittes
    :param depth: Rekursionstiefe
    :return: Nichts
    """
    counter += 1
    rainbow(counter)
    if depth == 1:
        turtle.forward(length)
        return
    turtle.right(45)
    draw_F(length, depth-1, counter)
    turtle.left(90)
    draw_F(length, depth-1, counter)
    turtle.right(45)


def fix_offset(length, depth):
    """
    Platziert die turtle so, dass Anfangs- und Enpunkt der Kurve
    gleich weit vom Mittelpunkt des Fensters entfernt sind.
    :param length: Länge eines Kurvenabschnittes
    :param depth: Rekursionstiefe
    :return: Nichts
    """
    # Anfangs- und Endpunkt entfernen sich um `length` * sqrt(2)^`depth`
    # Das heißt, wenn wir von diesem Wert die Hälfte ausrechnen,
    # erhalten wir den Wert, um den unsere turtle nach Links
    # gehen muss, um die Kurve mittig zu platzieren.
    offset = length * 2 ** (depth/2) // 2
    turtle.penup()
    turtle.backward(offset)
    turtle.pendown()


@save_canvas('levyc/levyc_rainbow_{pensize}_{depth}', turtle)
def draw_levy(length, depth=5, **kwargs):
    """
    Zeichnet die Lévy-C-Kurve.
    :param length: Länge jedes Streckenabschnittes
    :param depth: Rekursionstiefe
    :param kwargs: Turtle-Spezofikationen
    :return: Nicht
    """
    turtle.pen(**kwargs)
    fix_offset(length, depth)
    draw_F(length, depth)


if __name__ == '__main__':
    if not os.path.exists('./images/levyc'):
        os.mkdir('./images/levyc')
    draw_levy(1, depth=16, speed=0, shown=False, pensize=1)
    turtle.done()

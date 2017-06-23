"""
L-System der Lévy-C-Kurve

Winkel: 45°
Konstanten: F + -
Variablen: [x]
Ableitungsregeln:
    F -> + F - - F +
"""

import turtle
from save_result import save_canvas


def draw_F(length, depth):
    """
    Zeichnet rekursiv Streckenabschnitte.
    :param length: Länge des Streckenabschnittes
    :param depth: Rekursionstiefe
    :return: Nichts
    """
    if depth == 1:
        turtle.forward(length)
        return
    turtle.left(45)
    draw_F(length, depth-1)
    turtle.right(90)
    draw_F(length, depth-1)
    turtle.left(45)


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
    # erhalten wir den Wert, um den unsere turtle nach links
    # gehen muss, um die Kurve mittig zu platzieren.
    offset = length * 2 ** (depth/2) // 2
    turtle.penup()
    turtle.left(180)
    turtle.forward(offset)
    turtle.left(180)
    turtle.pendown()


# @save_canvas('levyC_curve_{depth}', turtle)
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
    draw_levy(1, depth=15, speed=0, shown=False)
    turtle.done()

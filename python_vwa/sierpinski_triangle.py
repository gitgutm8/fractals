import turtle
import itertools


def _draw_triangle(points):
    """
    Zeichnet ein Dreieck mithilfe vorgegebener Eckpunkte.
    :param points: Eckpunkte des Dreiecks
    :type points: list, tuple
    :return: Nicht
    :rtype: None
    """
    turtle.hideturtle()
    turtle.up()
    # Gehe zum dritten Punkt, um vernünftig mit der for-schleife
    # arbeiten zu können.
    turtle.goto(points[2])
    turtle.down()
    for point in points:
        turtle.goto(point)


def _middle(p1, p2):
    """
    Findet den Mittelpunkt zwischen zwei Punkten.
    :param p1: Erster Punkt
    :type p1: list, tuple
    :param p2: Zweiter Punkt
    :type p2: list, tuple
    :return: Mittelpunkt der beiden Punkte
    :rtype: list
    """
    # "Halbierter" Vektor von Punkt 1 zu Punkt 2 führt zum Mittelpunkt der beiden
    return [sum(components) / 2 for components in zip(p1, p2)]


def _triangle_generator(points):
    """
    Findet die nächstkleineren Dreiecke zum vorherigen.
    :param points: Punkte, für die Dreiecke generiert werden sollen
    :type points: list, tuple
    :return: Generator, der die drei Dreiecke liefert
    :rtype: iterator
    """
    return ([p0, _middle(p0, p1), _middle(p0, p2)]
            for p0, p1, p2 in
            # Wir nehmen nur jede zweite Permutation, da wir jeden Punkt nur
            # einmal als Ersten haben wollen. Der Generator selbst würde
            # insgesamt 6 Permutationen liefern.
            itertools.islice(itertools.permutations(points), 0, 6, 2))


def _sierpinski_triangle(points, depth):
    """
    Zeichnet Dreiecke, bis die gewünschte Rekursionstiefe erreicht ist.
    :param points: Eckpunkte des Dreiecks
    :type points: list, tuple
    :param depth: Rekursionstiefe
    :type depth: int
    :return: Nicht
    :rtype: None
    """
    if depth <= 0:
        return
    _draw_triangle(points)
    for triangle in _triangle_generator(points):
        _sierpinski_triangle(triangle, depth-1)


def sierpinski_triangle(start_points, depth=5, **kwargs):
    """
    Zeichet ein Sierpinskidreieck, ausgehend von Ecken des ersten Dreiecks.
    :param start_points: Eckepunkte des ersten Dreiecks
    :type start_points: list, tuple
    :param depth: Rekursionstiefe
    :type depth: int
    :param kwargs: turtle-Spezifikationen
    :return: Nichts
    :rtype: None
    """
    turtle.pen(**kwargs)
    _sierpinski_triangle(start_points, depth)
    turtle.done()


def sierpinski_from_side_length(side_length, **kwargs):
    """
    Zeichnet ein Sierpinskidreieck vom Wissen über die erste Seitenlänge aus.
    :param side_length: Länge der Seite des ersten Dreiecks
    :type side_length: int, float
    :param kwargs: Rekursionstiefe und turtle-Spezifikationen
    :return: Nichts
    :rtype: None
    """
    height = 3**0.5 * 0.5 * side_length
    p1 = 0, 0
    p2 = (side_length / 2, height)
    p3 = (side_length, 0)
    sierpinski_triangle((p1, p2, p3), **kwargs)


if __name__ == '__main__':
    # Punkte, die ein gleichseitiges Dreieck liefern
    example_points = [
        (  0,   0),
        (150, 260),  # 260 ist leicht gerundet
        (300,   0)
    ]
    # Lege die untere linke Ecke als Koordinatenursprung fest, ohne dabei
    # die größe des Fensters zu verändern.
    turtle.setworldcoordinates(0, 0, *turtle.screensize())
    sierpinski_from_side_length(300, depth=6, speed=0, pencolor='orange')

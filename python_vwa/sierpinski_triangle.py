import turtle
import itertools


def _draw_triangle(points):
    turtle.hideturtle()
    turtle.up()
    # Gehe zum dritten Punkt, um vernünftig mit der for-schleife
    # arbeiten zu können.
    turtle.goto(points[2])
    turtle.down()
    for point in points:
        turtle.goto(point)


def _middle(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    # Halber Vektor von Punkt 1 zu Punkt 2 führt zum Mittelpunkt der beiden
    return (x1+x2) / 2, (y1+y2) / 2


def _triangle_generator(points):
    return ([p0, _middle(p0, p1), _middle(p0, p2)]
            for p0, p1, p2 in
            # Wir nehmen nur jede zweite Permutation, da wir jeden Punkt nur
            # einmal als Ersten haben wollen. Der Generator selbst würde
            # insgesamt 6 Permutationen liefern.
            itertools.islice(itertools.permutations(points), 0, 6, 2))


def _sierpinski_triangle(points, depth):
    if depth <= 0:
        return
    _draw_triangle(points)
    for triangle in _triangle_generator(points):
        _sierpinski_triangle(triangle, depth-1)


def sierpinski_triangle(start_points, depth=5, **kwargs):
    turtle.pen(**kwargs)
    _sierpinski_triangle(start_points, depth)
    turtle.done()


def sierpinski_from_side_length(side_length, **kwargs):
    height = 3**0.5 * 0.5 * side_length
    p1 = 0, 0
    p2 = (side_length / 2, height)
    p3 = (side_length, 0)
    sierpinski_triangle((p1, p2, p3), **kwargs)


if __name__ == '__main__':
    example_points = [
        (  0,   0),
        (150, 260),
        (300,   0)
    ]
    # Lege die untere linke Ecke als Koordinatenursprung fest, ohne dabei
    # die größe des Fensters zu verändern.
    turtle.setworldcoordinates(0, 0, *turtle.screensize())
    sierpinski_from_side_length(300, depth=6, speed=0, pencolor='orange')

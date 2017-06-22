import turtle


def _draw_snowflake():
    pass





def snowflake(**kwargs):
    turtle.pen(**kwargs)
    turtle.begin_fill()
    _draw_snowflake()
    turtle.end_fill()


if __name__ == '__main__':
    snowflake(300, depth=6, speed=0, fillcolor='red', shown=False)
    turtle.done()

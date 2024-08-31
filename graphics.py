import turtle
import math

def draw_number_1(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.right(90)
    turtle_obj.forward(10*size*2)
    turtle_obj.up()

def draw_number_2(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_3(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.back(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_4(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.back(10*size)
    turtle_obj.back(10*size)
    turtle_obj.up()

def draw_number_5(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.back(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_6(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.back(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_7(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.forward(10*size)
    turtle_obj.up()
    turtle_obj.home()


def draw_number_8(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.left(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_9(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.up()

def draw_number_0(turtle_obj, pen_size, size):
    turtle_obj.width(pen_size)
    turtle_obj.down()
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size*2)
    turtle_obj.right(90)
    turtle_obj.forward(10*size)
    turtle_obj.right(90)
    turtle_obj.forward(10*size*2)
    turtle_obj.right(90)
    turtle_obj.right(45)
    turtle_obj.forward(math.sqrt((10*size*2)**2 + (10*size)**2))
    turtle_obj.up()
    turtle_obj.home()


def draw_number(turtle_obj, number, pen_size, size):
    if number == 1:
        draw_number_1(turtle_obj, pen_size, size)
    elif number == 2:
        draw_number_2(turtle_obj, pen_size, size)
    elif number == 3:
        draw_number_3(turtle_obj, pen_size, size)
    elif number == 4:
        draw_number_4(turtle_obj, pen_size, size)
    elif number == 5:
        draw_number_5(turtle_obj, pen_size, size)
    elif number == 6:
        draw_number_6(turtle_obj, pen_size, size)
    elif number == 7:
        draw_number_7(turtle_obj, pen_size, size)
    elif number == 8:
        draw_number_8(turtle_obj, pen_size, size)
    elif number == 9:
        draw_number_9(turtle_obj, pen_size, size)
    elif number == 0:
        draw_number_0(turtle_obj, pen_size, size)
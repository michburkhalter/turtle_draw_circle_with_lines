import math
import turtle

radius = 400
start_angle = 90
factor = 5
rotation_degrees = 360 * factor
nbr_of_points = 300 * factor


def connect_factor_function(nbr: float) -> float:
    """
    Insert function here
    :param nbr:
    :return:
    """
    res = nbr * factor
    return res


def print_position(x, y):
    print('{} {}'.format(x, y))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(str(x) + "," + str(y))


def calculate_coordinates(my_nbr_of_points, my_radius):
    angles = get_angles(my_nbr_of_points)
    my_points = []

    for angle in angles:
        x = (math.sin(math.radians(angle)) * my_radius)
        y = (math.cos(math.radians(angle)) * my_radius)
        my_points.append([x, y])

    return my_points


def get_angles(my_nbr_of_points):
    angles = []
    for n in range(my_nbr_of_points):
        angles.append((rotation_degrees / my_nbr_of_points) * n)

    return angles


def draw_line(my_t, start, end):
    # print("st {} en {}".format(start, end))

    my_t.penup()
    my_t.goto(start[0], start[1])
    my_t.pendown()
    # t.write(str(start[0]) + "," + str(start[1]))
    my_t.goto(end[0], end[1])


def calculate_points_to_connect(my_nbr_of_points):
    my_points_to_connect = []

    for x in range(my_nbr_of_points):
        nbr = x + 1
        # print(nbr)
        if connect_factor_function(nbr) < my_nbr_of_points:
            my_points_to_connect.append([nbr, connect_factor_function(nbr)])

    return my_points_to_connect


def print_info_texts():
    t.penup()
    t.goto(-450, 350)
    t.pendown()
    t.write('Number of Points: {}'.format(nbr_of_points))

    t.penup()
    t.goto(-450, 330)
    t.pendown()
    t.write('Factor: {}'.format(factor))

    t.penup()
    t.goto(-450, 310)
    t.pendown()
    t.write('Rotations: {}'.format(int(rotation_degrees / 360)))


if __name__ == '__main__':
    # Initializing the turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.onclick(print_position)
    t.speed(0)

    tmp_factor = turtle.numinput('factor', 'Please enter the factor', 5)
    tmp_nbr_of_points = turtle.numinput('Number of Points', 'Please enter the number of points', 300)
    try:
        factor = int(tmp_factor)
        rotation_degrees = 360 * factor
        nbr_of_points = int(tmp_nbr_of_points) * factor
    except ValueError:
        pass

    points = calculate_coordinates(nbr_of_points, radius)
    points_to_connect = calculate_points_to_connect(nbr_of_points)
    # print(points)
    print('there are {} lines to draw'.format(len(points_to_connect)))
    print('points_to_connect {}'.format(points_to_connect))

    # print info texts
    print_info_texts()

    # offset center of circle to [0,0]
    t.penup()
    t.goto(0, -1 * radius)
    t.pendown()

    # draw radius
    t.circle(radius)

    for line in points_to_connect:
        draw_line(t, points[line[0]], points[line[1]])

    turtle.done()

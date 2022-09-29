import math
import turtle

radius = 300
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


def calculate_coordinates(nbr_of_points, radius):
    angles = get_angles(nbr_of_points)
    points = []

    for angle in angles:
        x = (math.sin(math.radians(angle)) * radius)
        y = (math.cos(math.radians(angle)) * radius)
        points.append([x, y])

    return points


def get_angles(nbr_of_points):
    angles = []
    for n in range(nbr_of_points):
        angles.append((rotation_degrees / nbr_of_points) * n)

    return angles


def draw_line(t, start, end):
    # print("st {} en {}".format(start, end))

    t.penup()
    t.goto(start[0], start[1])
    t.pendown()
    # t.write(str(start[0]) + "," + str(start[1]))
    t.goto(end[0], end[1])


def calculate_points_to_connect(nbr_of_points):
    points_to_connect = []

    for x in range(nbr_of_points):
        nbr = x + 1
        # print(nbr)
        if connect_factor_function(nbr) < nbr_of_points:
            points_to_connect.append([nbr, connect_factor_function(nbr)])

    return points_to_connect


def print_info_txts():
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

    points = calculate_coordinates(nbr_of_points, radius)
    points_to_connect = calculate_points_to_connect(nbr_of_points)
    # print(points)
    print('there are {} lines to draw'.format(len(points_to_connect)))
    print('points_to_connect {}'.format(points_to_connect))

    # print info txts
    print_info_txts()

    # offset center of circle to [0,0]
    t.penup()
    t.goto(0, -1 * radius)
    t.pendown()

    # draw radius
    t.circle(radius)

    for line in points_to_connect:
        draw_line(t, points[line[0]], points[line[1]])

    turtle.done()

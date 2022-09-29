import math
import turtle

nbr_of_points = 16
factor = 2
radius = 150
start = [-150, 0]
start_angle = 90
last_point = start


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
        x = int(math.sin(math.radians(angle)) * radius)
        y = int(math.cos(math.radians(angle)) * radius)
        points.append([x, y])

    return points


def get_angles(nbr_of_points):
    angles = []
    angle = 0
    for n in range(nbr_of_points):
        angles.append((360 / nbr_of_points) * n)

    return angles


def draw_line(t, start, end):
    print("st {} en {}".format(start, end))

    t.penup()
    t.goto(start[0], start[1])
    t.pendown()
    t.write(str(start[0]) + "," + str(start[1]))
    t.goto(end[0], end[1])


if __name__ == '__main__':
    # Initializing the turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.onclick(print_position)

    points = calculate_coordinates(nbr_of_points, radius)
    last_point = points[len(points)-1]
    print(points)
    print(last_point)

    # offset center of circle to [0,0]
    t.penup()
    t.goto(0, -150)
    t.pendown()

    # draw radius
    t.circle(radius)

    for point in points:
        draw_line(t, last_point, point)
        last_point = point

    turtle.done()

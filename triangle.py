"""Functions about triangles."""


from math import sqrt


def special_right_triangles(n):
    """
    Generate up to n amount of 
    special right triangles ordered 
    by increasing total perimeter.
    """
    return [
        (x, y, z)
        for x in range(1, n)
        for y in range(x, n)
        for z in range(y, n)
        if x**2 + y**2 == z**2
    ]


def special_right_triangles_gen(n):
    """
    Generator for n amount of 
    special right triangles ordered 
    by increasing total perimeter.
    """
    yield from [
        (x, y, z)
        for x in range(1, n)
        for y in range(x, n)
        for z in range(y, n)
        if x**2 + y**2 == z**2
    ]


def isosceles_triangles(n):
    """
    Generate up to n amount of 
    special right triangles ordered 
    by increasing total perimeter.
    """
    return [
        (x, x, "sqrt({0:d})".format(2 * x**2))
        for x in range(1, n)
    ]


def isosceles_triangles_gen(n):
    """
    Generator for to n amount of 
    special right triangles ordered 
    by increasing total perimeter.
    """

    yield from [
        (x, x, "sqrt({0:d})".format(2 * x**2))
        for x in range(1, n)
    ]

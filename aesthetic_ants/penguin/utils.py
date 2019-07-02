# Contains utility functions
import math
import pyglet


def angle_between(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Returns the angle between the coordinates (x1, y1) and (x2, y2) in radians
    """
    dx = x2 - x1
    dy = y2 - y1

    # We return negative because pyglet and math treat rotation differently
    return -math.atan2(dy, dx)


def distance_between(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Returns the distance between the two points (x1, y1) and (x2, y2)
    """
    return distance_between_sq(x1, y1, x2, y2)**0.5


def distance_between_sq(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Returns the squared distance between the two points (x1, y1) and (x2, y2)
    """
    dx = x2 - x1
    dy = y2 - y1
    return dx**2 + dy**2


loader = pyglet.resource.Loader(path="../resources")

keys = pyglet.window.key.KeyStateHandler()

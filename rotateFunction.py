import numpy as np
from typing import Tuple


def rotate_function(p1: Tuple[float, float, float], p2: Tuple[float, float, float], x: np.ndarray, y: np.ndarray,
                    z: np.ndarray, alpha: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Rotate a meshgrid points (x, y, z) in 3D space around line defined by two points (p1, p2) by angle alpha (in radians)
    :param p1: First 3D point of line, around which to rotate (x, y, z)
    :param p2: Second 3D point of line, around which to rotate (x, y, z)
    :param x: 2D Array of x coordinates of points to rotate
    :param y: 2D Array of y coordinates of points to rotate
    :param z: 2D Array of z coordinates of points to rotate
    :param alpha: Angle in radians
    :return: Rotated points (x, y, z)
    """
    # Calculate vector of line
    v = np.array(p2) - np.array(p1)
    # Calculate unit vector of line
    v = v / np.linalg.norm(v)

    # Calculate rotation matrix
    c = np.cos(alpha)
    s = np.sin(alpha)
    t = 1 - c
    R = np.array([[t * v[0] ** 2 + c, t * v[0] * v[1] - s * v[2], t * v[0] * v[2] + s * v[1]],
                  [t * v[0] * v[1] + s * v[2], t * v[1] ** 2 + c, t * v[1] * v[2] - s * v[0]],
                  [t * v[0] * v[2] - s * v[1], t * v[1] * v[2] + s * v[0], t * v[2] ** 2 + c]])

    # Calculate rotated points
    x_rot = R[0, 0] * (x - p1[0]) + R[0, 1] * (y - p1[1]) + R[0, 2] * (z - p1[2]) + p1[0]
    y_rot = R[1, 0] * (x - p1[0]) + R[1, 1] * (y - p1[1]) + R[1, 2] * (z - p1[2]) + p1[1]
    z_rot = R[2, 0] * (x - p1[0]) + R[2, 1] * (y - p1[1]) + R[2, 2] * (z - p1[2]) + p1[2]

    return x_rot, y_rot, z_rot

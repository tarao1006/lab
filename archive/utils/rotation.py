from numbers import Number
from collections.abc import Container
import numpy as np
from functools import partial
from dataclasses import dataclass


@dataclass
class Quaternion:
    q0: float
    q1: float
    q2: float
    q3: float

    def __repr__(self):
        return f'{{{self.q0}, {self.q1}, {self.q2}, {self.q3}}}'


def _shift(radian: float) -> float:
    """Convert degree from kapsel coordinate to polar coodinate.

    Parameters
    ----------
    radian: flaot
        Degree to be changed coodinate system.

    Returns
    -------
    float
        Degrees changed coodinate system.
    """
    if radian >= 0 and radian <= np.pi / 2:
        return np.pi / 2 - radian
    elif radian >= np.pi / 2 and radian <= 2 * np.pi:
        return 5 / 2 * np.pi - radian


def shift_phases(radians: list) -> list:
    """Convert degree sequence from kapsel coordinate to polar coodinate.

    Parameters
    ----------
    radians: sequence of number
        Degrees to be changed coodinate system.

    Returns
    -------
    ndarray of number
        Degrees changed coodinate system.

    Raises
    ------
    TypeError:
        If argument is not sequence or sequence's contents are not number
    """
    if isinstance(radians, Number):
        radians = [radians]
    if not isinstance(radians, Container):
        raise TypeError(f"'{radians}' is not sequence of number, but {type(radians)}")

    shifted_radians = np.zeros(len(radians))
    for i, radian in enumerate(radians):
        if not isinstance(radian, Number):
            raise TypeError(f"'{radian}' is not numbers")
        radian = float(radian)
        shifted_radians[i] = _shift(radian)

    return shifted_radians


def angles_to_quaternion(yaw, pitch, roll) -> Quaternion:
    """Convert Euler angles to quaternions.

    Parameters
    ----------
    yaw: float
        z_axist rotation
    pitch: float
        y_axist rotation
    roll: float
        x_axist rotation

    Returns
    -------
    Quaternion
    """
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    q0 = cy * cp * cr + sy * sp * sr
    q1 = cy * cp * sr - sy * sp * cr
    q2 = sy * cp * sr + cy * sp * cr
    q3 = sy * cp * cr - cy * sp * sr

    return Quaternion(q0, q1, q2, q3)


x_rotation = partial(angles_to_quaternion, yaw=0.0, pitch=0.0)
y_rotation = partial(angles_to_quaternion, yaw=0.0, roll=0.0)
z_rotation = partial(angles_to_quaternion, pitch=0.0, roll=0.0)

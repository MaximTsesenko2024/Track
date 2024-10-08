"""Расчёт траектории полёта тела"""
from matplotlib import pyplot as plt
import numpy as np
import math


def calc(v, a):
    """
    Расчёт значений координат
    :param v: начальная скорость тела
    :param a: угол между вектром скорости и горизонтом
    :return: x, y значения координат в процессе полёта
    """
    g = 9.81
    a = math.radians(a)
    t_end = 2 * v * math.sin(a) / g
    t = np.linspace(0, t_end, 100)
    x = v * math.cos(a) * t
    y = v * math.sin(a) * t - g * t * t / 2
    return x, y


def show(x, y):
    ax = plt.subplot()
    ax.set_title = 'График полёта тела'
    ax.plot(x, y)
    plt.show()


def fly(v, a):
    show(*calc(v, a))

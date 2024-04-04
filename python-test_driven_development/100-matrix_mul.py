#!/usr/bin/python3
"""
    The `Matrix multiplication` module
"""


def matrix_mul(m_a, m_b):
    """
        Method that multiplies two matrixes
    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if not all(type(row) == list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) == list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul_array = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            num = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(num)
        mul_array.append(row)

    return mul_array

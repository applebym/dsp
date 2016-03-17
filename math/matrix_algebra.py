# Matrix Algebra

from sympy import *

A = Matrix([[1,2,3],[2,7,4]])
B = Matrix([[1,-1],[0,1]])
C = Matrix([[5,-1],[9,1],[6,0]])
D = Matrix([[3,-2,-1],[1,2,3]])
u = Matrix([[6, 2,-3,5]])
v = Matrix([[3,5,-1,4]])
w = Matrix([1,8,0,5])

def find_dim(m):
    print(m.shape)


def vec_ops(alpha=6):
    print(u + v)
    print(u - v)
    print(alpha * u)
    print(u.dot(v))
    print(u.norm())


def mat_ops():
    try:
        print(A + C)
    except ShapeError:
        print('Not Defined.')

    try:
        print(A - C.T)
    except ShapeError:
        print('Not Defined.')

    try:
        print(C.T + 3 * D)
    except ShapeError:
        print('Not Defined.')

    try:
        print(B * A)
    except ShapeError:
        print('Not Defined.')

    try:
        print(B * A.T)
    except ShapeError:
        print('Not Defined.')

    try:
        print(B * C)
    except ShapeError:
        print('Not Defined.')
    try:
        print(C * B)
    except ShapeError:
        print('Not Defined.')

    try:
        print(B * B * B * B)
    except ShapeError:
        print('Not Defined.')

    try:
        print(A * A.T)
    except ShapeError:
        print('Not Defined.')

    try:
        print(D.T * D)
    except ShapeError:
        print('Not Defined.')


def main():
    """
    Q1: Find the dimensions of each matrix

    Output:
    Q1
    (2, 3)
    (2, 2)
    (3, 2)
    (2, 3)
    (1, 4)
    (4, 1)
    """
    print('Q1')
    for m in [A, B, C, D, u, w]:
        find_dim(m)
    print()

    """
    Q2: Perform the following operations; alpha = 6

    Output:
    Q2
    Matrix([[9, 7, -4, 9]])
    Matrix([[3, -3, -2, 1]])
    Matrix([[36, 12, -18, 30]])
    51
    sqrt(74)
    """
    print('Q2')
    vec_ops()
    print()

    """
    Q3: Evaluate the following expressions

    Output:
    Q3
    Not Defined.
    Matrix([[-4, -7, -3], [3, 6, 4]])
    Matrix([[14, 3, 3], [2, 7, 9]])
    Matrix([[-1, -5, -1], [2, 7, 4]])
    Not Defined.
    Not Defined.
    Matrix([[5, -6], [9, -8], [6, -6]])
    Matrix([[1, -4], [0, 1]])
    Matrix([[14, 28], [28, 69]])
    Matrix([[10, -4, 0], [-4, 8, 8], [0, 8, 10]])
    """
    print('Q3')
    mat_ops()

if __name__ == '__main__':
    main()
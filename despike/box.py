# -*- coding: utf-8 -*-
import numpy as np


def box(A, i, j, size=1, nan=False):
    '''
    Extract the box (subarray) around (i,j) value inside
    a box of size `size` and replace the centrale
    value by NaN if necessary [option].
    '''
    if not isinstance(A, (list, np.ndarray)):
        raise TypeError(
            'The input must be an array. {} provided'.format(type(A)))

    ny, nx = A.shape
    if i < 0:
        raise ValueError('Line index `i` must be ≥ 0')
    if j < 0:
        raise ValueError('Column index `j` must be ≥ 0')
    if i >= nx:
        raise ValueError('Line index `i` must be < {}'.format(nx))
    if j >= ny:
        raise ValueError('Column index `j` must be < {}'.format(ny))

    if not isinstance(size, int):
        raise TypeError('Size must be an int')
    if size < 1:
        raise ValueError('The box size must be ≥ 1')

    if nan:
        # The change of type is required to store a NaN
        A = np.array(A, dtype=np.double)
        A[j, i] = np.nan

    l = i - size if i - size > 0 else 0
    r = i + size if i + size < nx else nx
    t = j - size if j - size > 0 else 0
    b = j + size if j + size < ny else ny

    return A[t:b+1, l:r+1]

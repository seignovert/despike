# -*- coding: utf-8 -*-
import pytest
import numpy as np

from despike.box import *


@pytest.fixture
def data():
    return np.arange(30).reshape(6, 5)
# [[ 0,  1,  2,  3,  4],
#  [ 5,  6,  7,  8,  9],
#  [10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24],
#  [25, 26, 27, 28, 29]]


def test_box(data):
    out = box(data, 1, 1)
    np.testing.assert_array_equal(out, [
        [0,  1,  2],
        [5,  6,  7],
        [10, 11, 12]
    ])


def test_box_size(data):
    out = box(data, 2, 2, size=2)
    np.testing.assert_array_equal(out, [
        [0,   1,  2,  3,  4],
        [5,   6,  7,  8,  9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24]
    ])


def test_box_nan(data):
    out = box(data, 1, 1, nan=True)
    np.testing.assert_array_equal(out, [
        [0,      1,  2],
        [5, np.nan,  7],
        [10,     11, 12]
    ])


def test_box_borders(data):
    out_i_0 = box(data, 0, 1)
    np.testing.assert_array_equal(out_i_0, [
        [0,  1],
        [5,  6],
        [10, 11]
    ])
    out_i_nx = box(data, 4, 1)
    np.testing.assert_array_equal(out_i_nx, [
        [3,  4],
        [8,  9],
        [13, 14]
    ])
    out_j_0 = box(data, 1, 0)
    np.testing.assert_array_equal(out_j_0, [
        [0, 1, 2],
        [5, 6, 7]
    ])
    out_j_ny = box(data, 1, 5)
    np.testing.assert_array_equal(out_j_ny, [
        [20, 21, 22],
        [25, 26, 27]
    ])


def test_box_err(data):
    with pytest.raises(TypeError):
        box(0, 1, 1)
    with pytest.raises(ValueError):
        box(data, -1, 1)
    with pytest.raises(ValueError):
        box(data, 1, -1)
    with pytest.raises(ValueError):
        box(data, 5, 1)
    with pytest.raises(ValueError):
        box(data, 1, 6)
    with pytest.raises(TypeError):
        box(data, 1, 1, size=1.)
    with pytest.raises(ValueError):
        box(data, 1, 1, size=-1)

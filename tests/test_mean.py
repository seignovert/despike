# -*- coding: utf-8 -*-
import pytest
import numpy as np

from despike.mean import *


@pytest.fixture
def img():
    return np.loadtxt('tests/data/img.dat')


def test_mask(img):
    out = mask(img)
    assert out.shape == img.shape
    assert out[0, 0] == False
    assert out[11, 46] == True
    np.testing.assert_allclose(img[out], [
        0.12458943, 0.07354096, 0.17214549,
        0.14881015, 0.12470777
    ], rtol=1e-7)


def test_mask_n(img):
    out = mask(img, n=5)
    np.testing.assert_allclose(img[out], [
        0.12458943, 0.17214549, 0.14881015, 0.12470777
    ], rtol=1e-7)


def test_mean(img):
    fill = mean(img)
    assert fill.shape == img.shape
    assert fill[11, 46] == 0.02855811407789588


def test_mean_size(img):
    fill = mean(img, size=2)
    assert fill.shape == img.shape
    assert fill[11, 46] == 0.02755289140623063

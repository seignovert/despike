# -*- coding: utf-8 -*-
import pytest
import numpy as np

from despike.despike import *


@pytest.fixture
def img():
    return np.loadtxt('tests/data/img.dat')


def test_spikes(img):
    out = spikes(img)
    assert out.shape == img.shape
    assert out[0, 0] == False
    assert out[11, 46] == True
    np.testing.assert_allclose(img[out], [
        0.04364175,  0.04325353,  0.05012336,  0.12458943,  0.05086355,
        0.00348282,  0.05014316,  0.00346915,  0.07354096,  0.01111674,
        0.02822303,  0.0035325,  0.03796474,  0.03840504,  0.03602542,
        0.03480986,  0.03781494,  0.17214549,  0.05080686,  0.00358726,
        0.02783948, -0.00499357,  0.03833514,  0.00414252,  0.03758394,
        -0.0045335,  0.03856845,  0.14881015,  0.12470777
    ], atol=1e-7)


def test_clean(img):
    out = clean(img)
    assert np.mean(out) == 0.023469550977608833
    assert np.std(out) == 0.00981149686482397
    assert np.median(out) == 0.021345600485801697


def test_clean_mask(img):
    out = clean(img, mask='median')
    assert np.mean(out) == 0.023507567118485895
    assert np.std(out) == 0.009739996632632463
    assert np.median(out) == 0.02135620918124914


def test_clean_fill(img):
    out = clean(img, fill_method='mean')
    assert np.mean(out) == 0.023468627164972132
    assert np.std(out) == 0.009806347117864314
    assert np.median(out) == 0.021345600485801697


def test_fill_err(img):
    with pytest.raises(ValueError):
        fill(img, np.zeros((2,2)))


def test_clean_err(img):
    with pytest.raises(ValueError):
        clean(img, mask='foo')
    with pytest.raises(ValueError):
        clean(img, fill_method='foo')


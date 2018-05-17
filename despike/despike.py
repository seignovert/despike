# -*- coding: utf-8 -*-
import numpy as np

from .box import box


def mean(A):
    return np.nanmean(A), np.nanstd(A)


def median(A):
    return np.nanmedian(A), np.nanstd(A)


def spikes(img, method='mean', size=2, n=3):
    '''
    Search spikes in the image using a moving box 
    of size `size` using `method` method with ± n × std
    '''

    if method.lower() == 'mean':
        mask = mean
    elif method.lower() == 'median':
        mask = median
    else:
        raise ValueError("The masking method must be '[mean|median]")

    ny, nx = img.shape
    _spikes = np.zeros((ny, nx))
    for i in range(nx):
        for j in range(ny):
            m, s = mask(box(img, i, j, size, nan=True))
            if img[j, i] < m - n * s or img[j, i] > m + n * s:
                _spikes[j, i] = 1

    return _spikes == 1


def fill(img, mask, method='mean', size=1):
    '''
    Fill the masked pixels with the mean value of
    surrounding neighboors inside a box of size `size`
    '''
    if img.shape != mask.shape:
        raise ValueError('Image and outlayers mask must have the same dimentsion: {} vs. {}'.format(
            img.shape, mask.shape
        ))

    if method.lower() == 'mean':
        f = np.nanmean
    elif method.lower() == 'median':
        f = np.nanmedian
    else:
        raise ValueError("The filling method must be '[mean|median]")

    A = np.copy(img)
    ny, nx = A.shape
    x, y = np.meshgrid(range(nx), range(ny))

    for x, y in zip(x[mask], y[mask]):
        A[y, x] = f(box(A, x, y, size=size, nan=True))
    return A


def clean(img, mask='mean', size=2, n=3, fill_method='median', fill_size=1):
    '''
    Clean image from spikes with the `fill_method` method with surrounding
    neighboors inside a box of size `fill_size`.
    '''
    return fill(img, spikes(img, mask, size, n), fill_method, fill_size)

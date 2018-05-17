# -*- coding: utf-8 -*-
import numpy as np

from .box import box
from .despike import fill

def mask(img, n=3):
    '''
    Search for outlayer pixels with a value lower/larger
    than the mean ± n × std
    '''
    med, std = np.nanmean(img), np.nanstd(img)
    return (img < (med - n * std)) | (img > (med + n * std))

def mean(img, n=3, size=1):
    '''
    Despike the image with a mean mask ± n × std
    '''
    return fill(img, mask(img, n), 'mean', size)

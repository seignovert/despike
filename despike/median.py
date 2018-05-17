# -*- coding: utf-8 -*-
import numpy as np

from .box import box
from .despike import fill

def mask(img, n=3):
    '''
    Search for outlayer pixels with a value lower/larger
    than the median ± n × std
    '''
    med, std = np.nanmedian(img), np.nanstd(img)
    return (img < (med - n * std)) | (img > (med + n * std))

def median(img, n=3, size=1):
    '''
    Despike the image with a median mask ± n × std
    '''
    return fill(img, mask(img, n), 'median', size)

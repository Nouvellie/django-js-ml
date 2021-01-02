from .pipeline import (
    Pipeline,
    register_in_pipeline,
)
from typing import Tuple

import numpy as np


@register_in_pipeline
def resize_img(img, target_size: Tuple = (28,28),):
    
    return img.resize(target_size)


@register_in_pipeline
def rescale_img(img, factor: float = 255.0,):
    img = np.array(img)/factor

    return img
from .pipeline import (
    Pipeline,
    register_in_pipeline,
)
from typing import Tuple

import numpy as np


# Functions
@register_in_pipeline
def resize_img(img, target_size: Tuple = (28,28),):
    return img.resize(target_size)


@register_in_pipeline
def rescale_img(img, factor: float = 255.0,):
    return np.expand_dims(np.array(img), axis=0) / factor
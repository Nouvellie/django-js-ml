from .utils import fromJSON

import importlib
import numpy as np


class InputsModelImage:
    '''
    Generate inputs for the current model
    '''
    def __init__(self, inputs_model_fromJSON=None,):
        self.inputs_model_fromJSON = inputs_model_fromJSON


    def img2input(self, img,):
        X = np.expand_dims(np.array(img), axis=0)        
        X = [X]

        return X


    def create_batch(self, list_images,):
        """Create batch list of numpy ecg to batches for the model"""
        list_inputs = [self.img2input(img) for img in list_images]

        batch = []
        axis_stack = 0
        
        for input_ in range(len(list_inputs[0])):
        
            batch.append(
                np.concatenate([X[input_] for X in list_inputs], axis=axis_stack)
            )

        return batch
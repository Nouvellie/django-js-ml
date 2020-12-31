from math import floor
from pathlib import Path
from typing import List, Union, Optional

import json
import numpy as np

#FIXME: output para una neurona de salida.
class DecoderOutput:
    '''
    Decode output of a model. Get the predicted classes using 'argmax' or 'umbral'
    
    argmax=True -> umbral is not use
    
    If you want to load a postprocessing from  a json file, instantiate the class without parameters
    >> decoder = DecoderOutput()
    >> decoder.fromJSON("path/to/postprocessing.json")

    Otherwise, provide the inputs for:
    
    Multiclass (many outputs, one choice)
    >> decoder = DecoderOutput(order_output_model = ["class1", "class2", "class3"], argmax = True)
    
    Using umbral for each class (if prediction[class]>umbral then return 1, otherwise return 0)
    >> decoder = DecoderOutput(order_output_model = ["class1", "class2", "class3"], umbral = 0.5)
    '''
    VERSION = 1

    def __init__(self, order_output_model: Optional[List[str]] = None, argmax: bool = False, umbral: Optional[Union[float, List[float]]] = None):
        self.order_output_model = order_output_model
        self.decode_output_by   = 'argmax' if argmax is True else 'umbral'
        self.umbral = umbral
        self.set_decoder_config()

    def set_decoder_config(self,):
        self.config = dict(
            order_output_model=self.order_output_model,
            decode_output_by=self.decode_output_by,
            umbral=self.umbral
            )

    def decode_by_argmax(self, output: List[float]):
        "Decode output using argmax"
        return [self.order_output_model[np.argmax(output)]]

    def decode_by_umbral(self, output: List[float]):
        "Decode output using umbral(s)"
        if isinstance(self.umbral, list):
            assert len(self.umbral)==len(self.order_output_model), 'list of umbrals does not have the same length than output'
            return [class_ for class_, pred, umbral in zip(self.order_output_model, output, self.umbral) if pred>=umbral]
        elif isinstance(self.umbral, float):
            return [class_ for class_, pred in zip(self.order_output_model, output) if pred>=self.umbral]
        else:
            raise("'umbral' must be a float or a list")

    def decode_output(self, output_model, include_confidence=False):
        """Decode output of the model

        Args:
            output_model (np.array): output of a keras model
            include_confidence (bool, optional): whether to return or not the output of the model. Defaults to False.

        Returns:
            dict: dictionary with the desired outputs
        """     
        # Take a list with the output of a keras model with one dense layer as output
        output_list = output_model[0].tolist()

        # Decode output by argmax (multiclass - 2 or more outputs / binary - 2 outputs)
        if self.decode_output_by == 'argmax':
            decoded_output = self.decode_by_argmax(output_list)
        
        # Decode output by umbral
        elif self.decode_output_by == 'umbral':
            # Special case: binary-1 output
            if len(output_list)==1:
                decoded_output = self.order_output_model[int(np.round(output_list[0]))]
            else:
                # multilabel-2+ outputs
                decoded_output = self.decode_by_umbral(output_list)

        # Output
        if include_confidence: 
            return dict(
                decoded_output=decoded_output, 
                confidence_model={class_: floor(output * 10 ** 4) / 10 ** 4
                            for class_, output 
                            in zip(self.order_output_model, output_list)
                            }
                )
        else:
            return dict(
                decoded_output=decoded_output
                )

    def asJSON(self, path_save=None):
        path_save = Path(path_save) if path_save else Path("postprocessing.json")
        with open(str(path_save), "w", encoding="utf8") as fp:
            json.dump(self.config, fp, indent=4, ensure_ascii=False)
        print(f"Postprocessing configuration saved at {path_save!r}")

    def fromJSON(self, path_postprocessing):
        # Rear postprocessing
        path_postprocessing = Path(path_postprocessing)
        with open(str(path_postprocessing), "r", encoding="utf8") as fp: 
            postprocessing = json.load(fp)
        
        self.order_output_model = postprocessing.get("order_output_model")
        self.decode_output_by   = postprocessing.get("decode_output_by")
        self.umbral = postprocessing.get("umbral")
        self.config = postprocessing
        print(f"Postprocessing loaded from {path_postprocessing!r}")

from .decoder_output import DecoderOutput  
from .file_loader import ImageLoader as FileLoader
from .inputs_model import InputsModelImage as InputsModel
from .preprocessing import (
    Pipeline, 
    register_in_pipeline,
)
from .utils import fromJSON
from abc import (
    ABCMeta, 
    abstractmethod,
)
from djangojsml.settings import  MODEL_ROOT
from math import floor
from pathlib import Path
from tensorflow import (
	convert_to_tensor,
	lite,
)
from tensorflow.keras.models import model_from_json
from time import time

import numpy as np
import os  
import re
import traceback


class BaseModelLoader(metaclass=ABCMeta):
    """Metaclass to define loaders for models"""
    def __init__(self, dir_model):
        self.dir_model=dir_model
        self.load_file_loader() # file to array
        self.load_preprocessing() # preprocess array
        self.load_input_model() # array as inputs for the model
        self.load_postprocessing() # get prediction based on classes
        self.preload_model()


    def load_file_loader(self,):
        """Function to load file as array"""
        self.file_loader = FileLoader()


    def load_input_model(self,):
        self.InputsModel = InputsModel()
    
    def load_preprocessing(self,):
        """Function to apply preprocessing to an array"""
        preprocessing_path = os.path.join(MODEL_ROOT + f"{self.dir_model}/preprocessing.json")
        
        self.preprocessing = Pipeline()
        self.preprocessing.fromJSON(preprocessing_path)


    def load_postprocessing(self,):
        """Function to apply postprocessing to the output of the model"""
        decoder_path = os.path.join(MODEL_ROOT + f"{self.dir_model}/postprocessing.json")
        self.decoder = DecoderOutput()
        self.decoder.fromJSON(decoder_path)


    def generate_input_model(self, input):
        """From file->array->preprocessing->input for the model"""
        
        input = self.file_loader(input)        
        input = self.preprocessing(input) 
        input = self.InputsModel.img2input(input)
        
        return input

    # @abstractmethod 
    # def preload_model(self,):
    #     pass

    # @abstractmethod 
    # def predict(self,):
    #     pass


class ModelLoaderTFLITE(BaseModelLoader):
    NUM_THREADS = 0

    def preload_model(self,):
        """Preload tflite model"""        
        name_tflite = [name for name in os.listdir(MODEL_ROOT + f"{self.dir_model}") if name.endswith(".tflite")][0]
        model_path = os.path.join(MODEL_ROOT + f"{self.dir_model}/{name_tflite}")
        
        if self.NUM_THREADS > 0:
            self.interpreter = lite.Interpreter(model_path=str(model_path), num_threads=self.NUM_THREADS)

        else:
            self.interpreter = lite.Interpreter(model_path=str(model_path))

        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()


    def predict(self, input, confidence_bool=False,):
        try:
            X = self.generate_input_model(input)

            for j,x in enumerate(X):
                input_X = convert_to_tensor(np.array(x), np.float32)
                
                self.interpreter.set_tensor(self.input_details[j]['index'], input_X)
            
            self.interpreter.invoke()
            
            prediction = self.interpreter.get_tensor(self.output_details[0]['index'])

            result = self.decoder.decode_output(prediction, include_confidence=confidence_bool)

            return result

        except Exception as e:
            full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())
            print(full_traceback, e)


class ModelLoaderJSONHDF5(BaseModelLoader):
    
    def preload_model(self,):
        json_model_path = os.path.join(MODEL_ROOT + f"{self.dir_model}/model.json")
        hdf5_model_path = os.path.join(MODEL_ROOT + f"{self.dir_model}/model.hdf5")

        # Generating model and graph for sessions
        with open(json_model_path, "r") as json_file:
            self.model = model_from_json(json_file.read())
        self.model.load_weights(hdf5_model_path)


    def predict(self, input, confidence_bool=False,):
        
        try:
            X = self.generate_input_model(input)

            prediction = self.model.predict(X)
            
            result = self.decoder.decode_output(prediction, include_confidence=confidence_bool)

            return result

        except Exception as e:
            full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())
            print(full_traceback, e)
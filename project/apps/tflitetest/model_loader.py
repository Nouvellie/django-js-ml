# Default imports
import re
import os
from math import floor

# Third party libs
import numpy as np
from time import time
from tensorflow import (
	convert_to_tensor,
	lite,
)
from PIL import Image
from djangojsml.settings import  MODEL_ROOT
from requirements.version import __version__
import traceback
from .preprocessing import (
    Pipeline, 
    register_in_pipeline,
)

from .decoder_output import DecoderOutput    

class ModelLoader:
    """
    How to use

    >> # Instantiate model
    >> model_loader = ModelLoader()
    >> interpreter_model , input_details_model, output_details_model = model_loader("modelname") # Nombre de la carpeta    
    """
    NUM_THREADS = 0

    def __init__(self, model_name):
        self.model_name=model_name
        self.preload_model()
        self.load_postprocessing()
        self.load_preprocessing()

    def load_preprocessing(self,):
        preprocessing_path = os.path.join(MODEL_ROOT + f"{self.model_name}/preprocessing.json")
        self.preprocessing = Pipeline()
        self.preprocessing.fromJSON(preprocessing_path)

    def load_postprocessing(self,):
        decoder_path = os.path.join(MODEL_ROOT + f"{self.model_name}/postprocessing.json")
        self.decoder = DecoderOutput()
        self.decoder.fromJSON(decoder_path)

    def preload_model(self,):
        model_path = os.path.join(MODEL_ROOT + f"{self.model_name}/model.tflite")
        print("asdasdasd")
        if self.NUM_THREADS > 0:
            self.interpreter = lite.Interpreter(model_path=model_path, num_threads=self.NUM_THREADS)
        else:
            self.interpreter = lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        #print(f"Model {self.model_name}")
        
    def predict(self, input, confidence_bool=False,):
        
        try:
            # Pre-processing
            array_image = self.load_image(input)

            # Predict
            input_images = convert_to_tensor(np.array(array_image), np.float32)
            self.interpreter.set_tensor(self.input_details[0]['index'], input_images)
            
            self.interpreter.invoke()
            
            prediction = self.interpreter.get_tensor(self.output_details[0]['index'])
            
        except Exception as e:
            full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())
            print(full_traceback)

        result = self.decoder.decode_output(prediction, include_confidence=confidence_bool)
        # result = {
        #     # Other options:
        #     "prediction": class_names[np.argmax(prediction)],
        #     "confidence": floor(prediction[0][np.argmax(prediction)] * 10 ** 4) / 10 ** 4,
        #     "filename": filename,
        #     "runtime": round(time.time() - start_time, 2),
        #     "version": __version__,
        # }
        
        return result

    def load_image(self, img,):
        #TODO: Modularizar las cargas, una para ecg, otra para imagenes, otra para X
        # load_img, load_ecg, load_X, ...
        """Load image from InMemoryUploadFile"""

        img = Image.open(img[0])
        gray_img = img.convert('L')
        array_image = self.preprocessing(gray_img)
        #array_image = self.pre_processing(gray_img)
        return array_image
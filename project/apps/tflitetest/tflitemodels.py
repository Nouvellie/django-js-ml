from .model_loader import ModelLoader
from .preprocessing import (
    Pipeline, 
    register_in_pipeline,
)
from djangojsml.settings import (
    MODEL_ROOT,
)
from math import floor
from PIL import Image
from requirements.version import __version__
from tensorflow import (
    convert_to_tensor,
    lite,
)

import numpy as np
import os
import re
import time
import traceback


# ----------------------------------------------------------- PRELOAD ----------------------------------------------------------- #
# Core preload
fashion_mnist_model = ModelLoader("fashionmnist")

# TFlite models
# interpreter_fashion_mnist , input_details_fashion_mnist, output_details_fashion_mnist = model_loader("fashionmnist")

## FASHION MNIST LABELS
class_names = ['t-shirt-top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle-boot']

# PIPELINE PREPROCESSING
preprocessing_mnist = Pipeline()
preprocessing_mnist.fromJSON(MODEL_ROOT + "fashionmnist/preprocessing.json")


# class MachineLearningTFLite():
    
#     def fashion_mnist_tflite(self, img_buffer, filename, start_time,):            

#         try:
#             # Pre-processing
#             array_image = self.load_image(img_buffer)

#             # Predict
#             input_images = convert_to_tensor(np.array(array_image), np.float32)
#             interpreter_fashion_mnist.set_tensor(input_details_fashion_mnist[0]['index'], input_images)
            
#             interpreter_fashion_mnist.invoke()
            
#             prediction = interpreter_fashion_mnist.get_tensor(output_details_fashion_mnist[0]['index'])
            
#         except Exception as e:
#             full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())
#             print(full_traceback)

#         result = {
#             # Other options:
#             "prediction": class_names[np.argmax(prediction)],
#             "confidence": floor(prediction[0][np.argmax(prediction)] * 10 ** 4) / 10 ** 4,
#             "filename": filename,
#             "runtime": round(time.time() - start_time, 2),
#             "version": __version__,
#         }
        
#         return result

    
#     def load_image(self, img_buffer,):

#         img = Image.open(img_buffer[0])
#         gray_img = img.convert('L')
#         array_image = preprocessing_mnist(gray_img)

#         return array_image
from djangojsml.settings import MEDIA_ROOT
from math import floor
from PIL import Image
from requirements.mlmodels import (
    FASHION_MNIST_TFLITE,
)
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

## FASHION MNIST
full_path_fashion_mnist = os.path.join(MEDIA_ROOT + FASHION_MNIST_TFLITE)
interpreter_fashion_mnist = lite.Interpreter(model_path=full_path_fashion_mnist)#, num_threads=4)
interpreter_fashion_mnist.allocate_tensors()
input_details_fashion_mnist = interpreter_fashion_mnist.get_input_details()
output_details_fashion_mnist = interpreter_fashion_mnist.get_output_details()

class_names = ['t-shirt-top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle-boot']


class MachineLearningTFLite():


    def fashion_mnist_tflite(self, img_buffer, filename, start_time,):            

        try:
            # Pre-processing
            array_image = self.load_image(img_buffer)

            # Predict
            input_images = convert_to_tensor(np.array(array_image), np.float32)
            interpreter_fashion_mnist.set_tensor(input_details_fashion_mnist[0]['index'], input_images)
            
            interpreter_fashion_mnist.invoke()
            
            prediction = interpreter_fashion_mnist.get_tensor(output_details_fashion_mnist[0]['index'])
            
        except Exception as e:
            full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())
            print(full_traceback)

        result = {
            # Other options:
            "prediction": class_names[np.argmax(prediction)],
            "confidence": floor(prediction[0][np.argmax(prediction)] * 10 ** 4) / 10 ** 4,
            "filename": filename,
            "runtime": round(time.time() - start_time, 2),
            "version": __version__,
        }
        
        return result

    
    def load_image(self, img_buffer,):

        img = Image.open(img_buffer[0])
        gray_img = img.convert('L')
        
        array_image = self.pre_processing(gray_img)

        return array_image

    
    def pre_processing(self, gray_img, target_size=(28, 28), rescale_factor=255.0,):

        img = gray_img.resize(target_size)
        array_image = np.expand_dims(np.array(img), axis=0) / rescale_factor

        return array_image
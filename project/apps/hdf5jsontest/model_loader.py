from djangojsml.settings import  MODEL_ROOT
from keras.models import model_from_json

import numpy as np
import os
import tensorflow as tf


# # Fashion Mnist
# with open(MEDIA_MODEL + "fashionmnist/model.json", "r") as json_file:
#     fashion_mnist_model = model_from_json(json_file.read())
# fashion_mnist_model.load_weights(MEDIA_MODEL + "fashionmnist/model.hdf5")
# fashion_mnist_graph = tf.get_default_graph()


class ModelLoader():

    def __init__(self, model_name,):
        self.model_name=model_name
        self.preload_model()
        # self.load_postprocessing()
        # self.load_preprocessing()
        # print(f"The model {model_name.title()} has been pre-loaded successfully.")


    def preload_model(self,):
        json_model_path = os.path.join(MODEL_ROOT + f"{self.model_name}/model.json")
        hdf5_model_path = os.path.join(MODEL_ROOT + f"{self.model_name}/model.hdf5")
        
        # Generating model and graph for sessions
        with open(json_model_path, "r") as json_file:
            self.model = model_from_json(json_file.read())
        self.model.load_weights(hdf5_model_path)
        # print(self.model.summary())
        # print(self.model.layers())
        # self.graph = tf.get_default_graph()


    def predict(self,):

        from tensorflow import keras
        data = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = data.load_data()
        import random
        i = random.choice([1,2,3,4,5,6,7,8,9])
        array_image = test_images[i]/255.0
        # print(self.model)
        # print(self.model.inputs)
        
        print(test_labels[i])
        predict = self.model.predict(array_image.reshape(1, 28, 28))
        print(np.argmax(predict[0]))
        predict = 'asd'
        return predict
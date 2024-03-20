import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model

import numpy as np




def processing_image(img_path):
   

#Load and preprocess the image
    img = image.load_img(img_path, target_size=(120, 120))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def load_model():
 #  Load the VGG16 model
    base_model = VGG16(weights='imagenet', include_top=False,input_shape=(120,120,3))
    model = Model(inputs=base_model.input, outputs=base_model.output)
    return model

def extract_features(model, preprocessed_img):
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / np.linalg.norm(flattened_features)
    return normalized_features






    

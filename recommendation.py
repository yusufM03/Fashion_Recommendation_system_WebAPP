from scipy.spatial.distance import cosine
from  utils import extract_features,processing_image,load_model
import numpy as np
import os


def recommend_fashion_items(input_image_path, all_features, all_image_names, model):
    # pre-process the input image and extract features
    
    preprocessed_img = processing_image(input_image_path)
    model=load_model()
    input_features = extract_features(model, preprocessed_img)
    print("donnnnnnnnnne")
    # calculate similarities and find the top N similar images
    similarities = [1 - cosine(input_features, other_feature) for other_feature in all_features]
    similar_indices = np.argsort(similarities)[-3:]
    #redfine path input image
    
    # filter out the input image index from similar_indices
    #similar_indices = [idx for idx in similar_indices if idx != all_image_names.index(input_image_path)]

    

    return [all_image_names[i] for i in similar_indices]



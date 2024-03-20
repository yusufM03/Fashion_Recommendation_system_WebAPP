from utils import processing_image,extract_features,load_model
import os

def Dataset_features():
    data=os.path.join("static","img")
    model=load_model()
    # extraction features 
    features=[]
    images_names=[]
    for file in os.listdir(data):  # file=prodcutisming/...
            if file != "Icons":
                path_direc=os.path.join(data,file)
                                                    #doss=chocolat
                for doss in os.listdir(path_direc):
                    if os.path.isdir(os.path.join(path_direc,doss)) :
                        path=os.path.join(path_direc,doss)
                        for img in os.listdir(path):

                            img_path=os.path.join(path,img)
                            image_process=processing_image(img_path)
                            feature=extract_features(model,image_process)
                            features.append(feature)
                            images_names.append(img_path)

                    else:
                        img_path=os.path.join(path_direc,doss)
                        image_process=processing_image(img_path)
                        feature=extract_features(model,image_process)
                        features.append(feature)
                        images_names.append(img_path)
                       

    print(images_names[0])
    return features,images_names

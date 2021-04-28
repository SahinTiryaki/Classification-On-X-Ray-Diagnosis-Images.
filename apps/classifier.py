from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np
import os

# load model 
def load_model():
    return models.load_model("model/modelim.h5")

# get image , return image
def get_image(img_path):
    image = load_img(path=img_path,target_size=(196,196),grayscale = False)
    image = np.array(img_to_array(image))
    image = image/255
    image = image.reshape(1,196,196,3)


    return image

# return prediction and prediction percentange
def predict(model,image):
    image = get_image(image)
    preds = model.predict(image)
    normal =  round(preds[0][0]*100,3)
    anomaly = round( preds[0][1]*100,3)
    return normal,anomaly

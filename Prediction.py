#Import packages
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras

#Identify the model path
model_dir = 'model/' 


#load in model and weight 
weightfile = model_dir+'REIP.10-0.8500.hdf5' #reading the model you trained above
model = keras.models.load_model(model_dir+'REIP.h5') #load the basemodel, 
model.load_weights(weightfile) #add the weight file that just trained to the basemodel 
#create a model to predict the feature space. 



def prediction(image_folder_path): # ex : '/gdrive/My Drive/REIP/imagedata/clear/27.tif')
    '''This prediction function take input picture file and return the predicted class'''
    reip_dict = {0:'clear', 1:'blur', 2:'surface charge'}
    image = tf.keras.preprocessing.image.load_img(image_folder_path)
    np_image = cv2.resize(np.array(image)[0:890, :],(300,300)).astype('float32')/255
    input_arr = np.array([np_image])  # Convert single image to a batch.
    predictions = model(input_arr)
    predict = reip_dict.get(np.argmax(predictions[0]))
    pre_string = f'It is predicted to be {predict}.'
    return {pre_string:np_image}
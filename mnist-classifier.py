import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

filename = input("Enter image filename (with extension)\n")

img = cv2.resize(plt.imread(filename),(28,28))


from keras.models import load_model
model = load_model('CNN.h5')



def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

img_grayscale = rgb2gray(img).reshape(1,28,28,1)


pred = model.predict(img_grayscale)
print("Prediction: ", np.argmax(pred),"\n Confidence: ", pred[0,np.argmax(pred)])
input()
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow import keras
import time
import os

def preprocess_image(image_path):
	img = load_img(image_path, target_size=(224, 224))
	img = img_to_array(img) / 255.0
	img = np.expand_dims(img, axis=0) 
	img_arr = np.vstack([img])
	return img_arr

def main(filename):
	path = './flask_deep/static/images/uploaded/' + str(filename)
	img = preprocess_image(path)
	
	model = keras.models.load_model('./flask_deep/models/MobileNetV2.h5')
	# model = keras.models.load_model('./flask_deep/models/ResNet50.h5')

	result = np.argmax(model.predict(img))

	return result

def pred_to_kor(pred_result):
	li = ['습진', '흑색종', '아토피 피부염', '기저세포암', 
				'멜라닌 세포 모반', '지루성 각질 및 종양', '사마귀', '원숭이 두창'
				]

	return li[pred_result]
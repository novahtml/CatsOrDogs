import numpy as np
from tensorflow import keras
import tensorflow as tf


def dog_cat_predict(image_file):
  model = tf.keras.models.load_model('model2.h5')
  label_names = ["cat", "dog"]

  img = keras.preprocessing.image.load_img(image_file, target_size=(128, 128))
  img_arr = np.expand_dims(img, axis=0) / 255.0
  result = model.predict_classes(img_arr)
  return label_names[result[0][0]]
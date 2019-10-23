import numpy as np
from tensorflow import keras
import tensorflow as tf

def dog_cat_predict(model, image_file):
  label_names = ["cat", "dog"]

  img = keras.preprocessing.image.load_img(image_file, target_size=(128, 128))
  img_arr = np.expand_dims(img, axis=0) / 255.0
  result = model.predict_classes(img_arr)
  print("Result: %s" % label_names[result[0][0]])

model = tf.keras.models.load_model('dogs_cats.h5')
dog_cat_predict(model, "dog_test.jpg")
#dog_cat_predict(model, "train\dog.0.jpg")
import numpy as np
from tensorflow import keras
import tensorflow as tf

def dog_cat_predict(model, image_file):
  label_names = ["cat", "dog"]

  img = keras.preprocessing.image.load_img(image_file, target_size=(128, 128))
  img_arr = np.expand_dims(img, axis=0) / 255.0
  result = model.predict_classes(img_arr)
  print("Result: %s" % label_names[result[0][0]])

model = tf.keras.models.load_model('model2.h5')
dog_cat_predict(model, "dog_test.jpg")

#%% OR

from keras.models import model_from_json
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input


classes = ['cats', 'dogs']
json_file = open("model.json")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
loaded_model.compile(optimizer='rmsprop', loss='categorical_crossentropy',metrics=['accuracy'])

img = image.load_img("dog_tes.jpg", target_size=(224, 224))
 
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
#                      Запускаем распознавание
 
prediction = loaded_model.predict(x)
 
print(["%d%%" % i for i in np.round(prediction * 100)[0]])
print(classes[np.argmax(prediction)])

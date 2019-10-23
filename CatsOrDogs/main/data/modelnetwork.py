
from keras.preprocessing import image
from keras.models import Model, model_from_json
from keras.layers import Dense, GlobalAveragePooling2D
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
import numpy
from keras.applications.vgg16 import preprocess_input
 
# Размер изображений
img_width, img_height = 224, 224
# Путь к каталогу с изображениями для обучения
train_data_dir = 'train'
# Количество эпох
epochs = 1
# Размер выборки
batch_size = 1
 
# Загружаем сеть VGG16 без части, которая отвечает за классификацию
base_model = applications.VGG16(weights='imagenet', include_top=False)
 
# Добавляем слои классификации
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
# Выходной слой с двумя нейронами для классов "кот" и "собака"
predictions = Dense(2, activation='softmax')(x)
 
# Составляем сеть из двух частей
model = Model(inputs=base_model.input, outputs=predictions)
 
# "Замораживаем" сверточные уровни сети VGG16
# Обучаем только вновь добавленные слои
for layer in base_model.layers:
    layer.trainable = False
 
# Компилируем модель
model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
              metrics=['accuracy'])
 
# Создаем генератор данных для обучения
datagen = ImageDataGenerator(rescale=1. / 255, validation_split = 0.1)
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode= 'categorical',
    subset='training')
 
# Создаем генератор данных для валидации
validation_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode= 'categorical',
    subset='validation')
 
## Количество изображений для обучения
nb_train_samples = train_generator.samples
## Количество изображений для валидации
nb_validation_samples = validation_generator.samples
 
# Обучаем модель с помощью генератора
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples)
 
#%%
# Сохраняем нейронную сеть
print("Сохранить обученную нейросеть?")
symbol_2 = "a"
while symbol_2 != "y" and symbol_2 != "n":
    symbol_2 = input("Нажмите y, если хотите сохранить результаты обучения нейросети, либо n в противном случае\n")
if symbol_2 == "y":
    model_json = model.to_json()
    neuronet_filenames = input("Введите название для двух файлов, куда сохранится информация по нейросети\n>>")
    json_file = open("%s.json" % neuronet_filenames, "w")
    json_file.write(model_json)
    json_file.close()
    model.save_weights("%s.h5" % neuronet_filenames)
 
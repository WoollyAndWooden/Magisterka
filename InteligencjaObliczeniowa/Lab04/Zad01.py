from sys import argv
from os import listdir, makedirs
from pathlib import Path
from shutil import copyfile

from keras import Sequential, Model
from keras.src.applications.resnet import ResNet101
from keras.src.callbacks import ModelCheckpoint
from keras.src.layers import Conv2D, MaxPooling2D, Flatten, Dense, GlobalAveragePooling2D
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras.src.optimizers import SGD, Adam
from matplotlib import pyplot
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy.random import seed, random

folder = 'dogs-cats-mini/'
try:
    start = int(argv[1]) if 0 <= int(argv[1])  <= 20 else 0
except(IndexError, ValueError):
    start = 0

try:
    start2 = int(argv[2]) if 0 <= int(argv[2])  <= 20 else 0
except(IndexError, ValueError):
    start2 = 0


def Generate_npys():
    photos, labels = list(), list()

    for file in listdir(folder):
        output = 0.0
        if file.startswith('dog'):
            output = 1.0
        photo = load_img(folder + file, target_size=(200, 200))
        photo = img_to_array(photo)

        photos.append(photo)
        labels.append(output)

    photos = asarray(photos)
    labels = asarray(labels)
    print(photos.shape, labels.shape)
    save("dogs-cats-mini_photos.npy", photos)
    save("dogs-cats-mini_labels.npy", labels)

def summarize_diagnostics(history, name):
    pyplot.subplot(211)
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(history.history['loss'], color='blue', label='train')
    pyplot.plot(history.history['val_loss'], color='orange', label='test')
    pyplot.subplot(212)
    pyplot.title('Classification Accuracy')
    pyplot.plot(history.history['accuracy'], color='blue', label='train')
    pyplot.plot(history.history['val_accuracy'], color='orange', label='test')

    pyplot.tight_layout(pad=4.0)

    filename = name
    pyplot.savefig(filename + '_plot.png')
    pyplot.close()

#if not (Path('dogs-cats-mini_photos.npy').exists() or Path('dogs-cats-mini_labels.npy').exists()):
#    Generate_npys()

dataset_home = 'dataset_dvc/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
    labeldirs = ['dogs/', 'cats/']
    for labeldir in labeldirs:
        newdir = dataset_home + subdir + labeldir
        makedirs(newdir, exist_ok=True)

seed(278008)
val_ratio = 0.25
src_dir = "dogs-cats-mini/"
for file in listdir(src_dir):
    src= src_dir + '/' + file
    dst_dir = subdirs[0]
    if random() < val_ratio:
        dst_dir = subdirs[1]
    dst = dataset_home + dst_dir + file[:3] + 's/' + file
    if not Path(dst).exists():
        copyfile(src, dst)


def define_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu',
                     kernel_initializer="he_uniform", padding="same",
                     input_shape=(200, 200, 3)))
    model.add(Conv2D(64, (3, 3), activation='relu',
                     kernel_initializer="he_uniform", padding="same",
                     ))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer="he_uniform"))
    model.add(Dense(1, activation='sigmoid'))

    opt = SGD(learning_rate=0.001, momentum=0.9)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    checkpoint = ModelCheckpoint(
        "model1/model_base_{epoch:02d}.keras",
        save_weights_only=False,
        save_freq='epoch',
    )
    return model, checkpoint

model, checkpoint = define_model()

datagen = ImageDataGenerator(rescale=1.0/255.0)

train_iter = datagen.flow_from_directory(dataset_home + subdirs[0],
                                    class_mode='binary', batch_size=64,target_size=(200, 200))
test_iter = datagen.flow_from_directory(dataset_home + subdirs[1],
                                    class_mode='binary', batch_size=64,target_size=(200, 200))

history = model.fit(train_iter, steps_per_epoch=len(train_iter), epochs=20, validation_data=test_iter,
                    validation_steps=len(test_iter), verbose=0, callbacks=[checkpoint], initial_epoch=start)

_, acc = model.evaluate(test_iter, steps=len(test_iter), verbose=0)
print('> % .3f' % (acc * 100.0))

if not Path("Zad01_plot.png").exists():
    summarize_diagnostics(history, "Zad01")

zad02 = ResNet101(weights='imagenet', include_top=False, input_shape=(200, 200, 3))
x2 = zad02.output
x2 = GlobalAveragePooling2D()(x2)
x2 = Dense(128, activation='relu')(x2)
predictions = Dense(1, activation='sigmoid')(x2)

model = Model(inputs=zad02.input, outputs=predictions)
for layer in zad02.layers:
    layer.trainable = False

checkpoint = ModelCheckpoint(
        "model2/ResNet101_{epoch:02d}.keras",
        save_weights_only=False,
        save_freq='epoch',
    )

model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(train_iter, validation_data=test_iter, epochs=20, callbacks=[checkpoint], initial_epoch=start2)

_, acc = model.evaluate(test_iter, steps=len(test_iter), verbose=0)
print('> % .3f' % (acc * 100.0))

if not Path("Zad02_plot.png").exists():
    summarize_diagnostics(history, "Zad02")



import os
import glob
from sklearn.preprocessing import MultiLabelBinarizer
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import random

IMG_WIDTH, IMG_HEIGHT = 32, 32
IMG_DIM = (IMG_WIDTH, IMG_HEIGHT)

def get_data(image_folder_path):
    files = glob.glob(image_folder_path)
    random.shuffle(files)

    data_len = len(files)
    print("Datalen: " + str(data_len))

    labels = [fn.split('\\')[-1].split('_')[:2] for fn in files]
    labels = binarize_labels(labels)
    print("Labels binarized")

    imgs = resize_images(files)
    print("Images resized, scale: ", IMG_DIM)

    return imgs, labels

def resize_images(files):
    imgs = [img_to_array(load_img(img, target_size=IMG_DIM)) for img in files]
    return np.array(imgs).astype('float32') / 255

def binarize_labels(labels):

    no_labels = len(labels)

    f = open("all_categories.txt", "r")
    for line in f:
        output = line.split('_')
        labels.append([output[0], output[1][-2]])
    f.close()
    mlb = MultiLabelBinarizer()
    all_labels = np.array(labels)
    new_labels = mlb.fit_transform(all_labels)
    labels_of_interest = new_labels[:no_labels]

    return labels_of_interest

def plot_history(history):
    # Plot training & validation accuracy values
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
    
import matplotlib.pyplot as plt
    


from keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.applications.resnet_v2 import ResNet152V2
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import  Dense, Dropout, Flatten
from tensorflow.keras.callbacks import EarlyStopping

from data_handler import*

#Configurations for the best model

NO_UNFREEZED_LAYERS = 4
NO_DENSE_DROPOUT_LAYERS = 2
NO_NEURONS = 448
DROPOUT = 0.15
OPTIMIZER = 'sgd'
MODEL_NAME ='ResNet152V2_tuned.h5'


def build_model():
    ### ResNet
    resnet = ResNet152V2(include_top=False, weights='imagenet', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))

    output = resnet.layers[-1].output
    output = Flatten()(output)

    resnet = Model(resnet.input, outputs=output)

    for layer in resnet.layers[:-NO_UNFREEZED_LAYERS]:
        layer.trainable = False
    for layer in resnet.layers[-NO_UNFREEZED_LAYERS:]:
        layer.trainable = True
    model = Sequential()
    model.add(resnet)
    
    #CHANGE
    for i in range(NO_DENSE_DROPOUT_LAYERS):
        model.add(Dense(NO_NEURONS, activation='relu'))
        model.add(Dropout(DROPOUT))
        
  
    model.add(Dense(28, activation='sigmoid'))


    model.compile(loss='categorical_crossentropy',
                  optimizer=OPTIMIZER,
                  metrics=['accuracy'])

    return model

batch_size = 32


path_to_training_set = 'training/*'
path_to_test_set = 'testing/*'

train, train_labels = get_data(path_to_training_set)
test, test_labels = get_data(path_to_test_set)

aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")

img_gen_train = aug.flow(train, train_labels, batch_size=batch_size, shuffle=True)


callback = EarlyStopping(
    monitor="val_loss",
    min_delta=0,
    patience=2,
    verbose=0,
    mode="auto",
    restore_best_weights=True,
)

model = build_model()

EPOCHS = 1
history = model.fit_generator(
    img_gen_train,
    validation_data=(test, test_labels),
    steps_per_epoch=None,
    callbacks = [callback],
    epochs=EPOCHS, verbose=2)

plot_history(history)
model.save(MODEL_NAME)



#do something to model
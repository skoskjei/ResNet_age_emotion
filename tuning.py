
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.applications.resnet_v2 import ResNet152V2
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten

from kerastuner.tuners import RandomSearch, Hyperband
from kerastuner.engine.hyperparameters import HyperParameters

from kerastuner.applications import HyperResNet
import pickle
from data_handler import*

DIR_NAME = "tuning"
PROJECT_NAME = "HyperRestNet"


batch_size = 32

train, train_labels = get_data('training/*')
test, test_labels = get_data('testing/*')
print("Original images in use: training: " + str(len(train)) + ", testing: " + str(len(test)))
# Reduced data for code testing purposes

### ImageDataGenerator
aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")

img_gen_train = aug.flow(train, train_labels, batch_size=batch_size, shuffle=True)

#This model is not currently used
def build_model(hp):
    ### ResNet
    resnet = ResNet152V2(include_top=False, weights='imagenet', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))

    output = resnet.layers[-1].output
    output = Flatten()(output)

    resnet = Model(resnet.input, outputs=output)

    used_layers = hp.Int('num_layers',3,6)

    for layer in resnet.layers[:-used_layers]:
        layer.trainable = False
    for layer in resnet.layers[-used_layers:]:
        layer.trainable = True

    model = Sequential()
    model.add(resnet)
    for i in range(hp.Int('num_layers_2',1,4)):
        model.add(Dense(units=hp.Int('units', min_value=32, max_value=512, step = 32), activation='relu'))
        model.add(
            Dropout(rate=hp.Float(
                'dropout',
                min_value=0.0,
                max_value=0.5,
                default=0.25,
                step=0.05,
            ))
        )

    model.add(Dense(28, activation='sigmoid'))

    optimizer = hp.Choice('optimizer', ['adam', 'sgd', 'rmsprop'])

    model.compile(
        loss='categorical_crossentropy',
        optimizer = optimizer,
        metrics=['accuracy'])
    return model

hyper_model = HyperResNet(input_shape=(IMG_WIDTH, IMG_WIDTH, 3), classes=28)

# Hyperband serach, could use Random Search instead

tuner = Hyperband( 
    hypermodel=hyper_model,
    objective="val_accuracy",
    max_epochs=5,
    directory=DIR_NAME,
    project_name=PROJECT_NAME
)
tuner.search_space_summary()
tuner.search(img_gen_train, validation_data =(test, test_labels))

tuner.results_summary()
best_model = tuner.get_best_models(num_models=1)[0]
best_model.summary()

with open("tuner"+PROJECT_NAME+".pkl", "wb") as f:
    pickle.dump(tuner, f)


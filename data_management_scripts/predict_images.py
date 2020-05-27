import cv2
import numpy as np
from keras.models import load_model
import glob, os


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def predict_images(model):
    num_of_imges = 0
    num_of_predicted_imges = 0
    num_of_angry = 0
    num_of_fear = 0
    num_of_happy = 0
    num_of_sad = 0
    num_of_surprised = 0
    num_of_neutral = 0
    newf = open("emotion_data_test.txt", "w+")

    # Dictionary for emotion recognition model output and emotions
    emotions = {0: 'Angry', 1: 'Fear', 2: 'Happy', 3: 'Sad', 4: 'Surprised', 5: 'Neutral'}

    olddir = os.getcwd()

    newdir = olddir + "\\face_age_add_age_test"
    os.chdir(newdir)

    for file in glob.glob("*.png"):
        image = rgb2gray(cv2.imread(file));
        test_image = cv2.resize(image, (48, 48))
        test_image = test_image.reshape([-1, 48, 48, 1])

        test_image = np.multiply(test_image, 1.0 / 255.0)
        probab = model.predict(test_image)[0] * 100
        # Finding label from probabilities
        # Class having highest probability considered output label
        label = np.argmax(probab)
        max_probab = probab[label]
        predicted_emotion = emotions[label]

        if max_probab >= 55:
            newf.write(str(file) + "-" + str(predicted_emotion))
            newf.write("\n")
            num_of_predicted_imges += 1
            if predicted_emotion == "Angry":
                num_of_angry += 1
            elif predicted_emotion == "Fear":
                num_of_fear += 1
            elif predicted_emotion == "Happy":
                num_of_happy += 1
            elif predicted_emotion == "Sad":
                num_of_sad += 1
            elif predicted_emotion == "Surprised":
                num_of_surprised += 1
            elif predicted_emotion == "Neutral":
                num_of_neutral += 1

        num_of_imges += 1

    newf.close()
    print("Total number of pictures: " + str(num_of_imges))
    print("Number of labeled pictures: " + str(num_of_predicted_imges))
    print("Distribution of emotions: ")
    print("Angry: " + str(num_of_angry))
    print("Fear: " + str(num_of_fear))
    print("Happy: " + str(num_of_happy))
    print("Sad: " + str(num_of_sad))
    print("Surprised: " + str(num_of_surprised))
    print("Neutral: " + str(num_of_neutral))


def main():
    # Creating objects for emotion detection
    emotion_model = load_model('./model/emotion_recognition.h5')
    predict_images(emotion_model)


if __name__ == '__main__':
    main()

import os
import glob
import random
import shutil


# Create directory
def create_directory(dir_name):
    try:
        # Create target Directory
        os.mkdir(dir_name)
        print("Directory ", dir_name, " Created ")
    except FileExistsError:
        print("Directory ", dir_name, " already exists")

def move_files(folder_name, training_percentage):
    files = glob.glob(folder_name)
    create_directory('training') # Source for storing training data
    create_directory('testing')

    for f in files:
        if random.random() < training_percentage:
            shutil.move(f,'training')
        else:
            shutil.move(f,'testing')


training_percentage = 0.8
image_folder_path = 'age_and_emotion/*'
move_files(image_folder_path, training_percentage)



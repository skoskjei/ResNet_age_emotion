import glob, os

olddir = os.getcwd()

newdir = olddir + "\\face_age_add_age_and_emotion_all\\"
os.chdir(newdir)

for ageint in range(1, 102):
    age = str(ageint)
    if len(age) != 3:
        if len(age) == 1:
            age = "00" + age
        elif len(age) == 2:
            age = "0" + age

    for file in glob.glob("*.png"):
        if file.startswith(age):
            if file.startswith(age+"_2"):
                os.remove(file)
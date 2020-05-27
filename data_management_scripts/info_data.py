import glob, os
import shutil

olddir = os.getcwd()

newf = open("info_data_2.txt", "w+")

newdir = olddir + "\\face_age_add_age_and_emotion_all\\"
os.chdir(newdir)

for ageint in range(1, 102):
    age = str(ageint)
    if len(age) != 3:
        if len(age) == 1:
            age = "00" + age
        elif len(age) == 2:
            age = "0" + age
    num_of_0 = 0
    num_of_1 = 0
    num_of_2 = 0
    num_of_3 = 0
    newf.write("Age " + age + ":")
    newf.write("\n")

    for file in glob.glob("*.png"):
        if file.startswith(age):
            if file.startswith(age+"_0"):
                num_of_0 += 1
            elif file.startswith(age+"_1"):
                num_of_1 += 1
            elif file.startswith(age+"_2"):
                num_of_2 += 1
            elif file.startswith(age+"_3"):
                num_of_3 += 1

    newf.write("0: " + str(num_of_0))
    newf.write("\n")
    newf.write("1: " + str(num_of_1))
    newf.write("\n")
    newf.write("2: " + str(num_of_2))
    newf.write("\n")
    newf.write("3: " + str(num_of_3))
    newf.write("\n")
    newf.write("Total: " + str(num_of_0+num_of_1+num_of_2+num_of_3))
    newf.write("\n")

newf.close()
import glob, os
import shutil

olddir = os.getcwd()
newdir = olddir + "\\face_age_add_age_and_emotion_all"
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
            if file.startswith(age+"_1"):
                filenamesplit = file.split("_")
                filenamept1 = filenamesplit[0]
                filenamept2 = filenamesplit[1]
                filenamept3 = filenamesplit[2]

                newfilename = str(filenamept1) + "_" + str(0) + "_" + str(filenamept3)

                destfile = olddir + "\\face_age_add_age_and_emotion_done\\" + newfilename
                shutil.move(file, destfile)

            elif file.startswith(age+"_0"):
                destfile = olddir + "\\face_age_add_age_and_emotion_done\\" + file
                shutil.move(file, destfile)


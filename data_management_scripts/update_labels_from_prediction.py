import glob, os
import shutil

f = open("emotion_data_all.txt", "r")
olddir = os.getcwd()
newdir = olddir + "\\face_age_add_age_all"
os.chdir(newdir)

for line in f:
    line = line.rstrip()
    line = line.split("-")
    filename = line[0]

    filenamesplit = filename.split("_")
    filenamept1 = filenamesplit[0]
    filenamept3 = filenamesplit[1]

    if line[1] == "Neutral":
        filenamept2 = "0"
    elif line[1] == "Angry" or line[1] == "Fear" or line[1] == "Sad": # These are all merged to "unhappy"
        filenamept2 = "1"
    elif line[1] == "Surprised":
        filenamept2 = "2"
    elif line[1] == "Happy":
        filenamept2 = "3"
    else:
        print("No emotion")
        break

    newfilename = str(filenamept1) + "_" + str(filenamept2) + "_" + str(filenamept3)

    destfile = olddir + "\\face_age_add_age_and_emotion_all\\" + newfilename
    shutil.move(filename, destfile)

f.close()

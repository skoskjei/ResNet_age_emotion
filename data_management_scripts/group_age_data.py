import glob, os
import shutil

olddir = os.getcwd()
newdir = olddir + "\\face_age_add_age_and_emotion_done"
os.chdir(newdir)

for file in glob.glob("*.png"):
    if file.startswith("072_") or file.startswith("073_") or file.startswith("074_") or file.startswith("075_") or file.startswith("076_") or file.startswith("077_") or file.startswith("078_"):
        #change to 1
        filenamesplit = file.split("_")
        filenamept2 = filenamesplit[1]
        filenamept3 = filenamesplit[2]

        newfilename = "25" + "_" + str(filenamept2) + "_" + str(filenamept3)

        destfile = olddir + "\\face_age_add_age_and_emotion_really_done_now_finito\\" + newfilename
        shutil.move(file, destfile)
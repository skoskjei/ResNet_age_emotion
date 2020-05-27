import glob, os
import shutil

olddir = os.getcwd()

for foldernr in range(1, 102):
    if foldernr != 94 and foldernr != 97 and foldernr != 98:
        foldername = str(foldernr)
        if len(foldername) != 3:
            if len(foldername) == 1:
                foldername = "00" + foldername
            elif len(foldername) == 2:
                foldername = "0" + foldername
        newdir = olddir + "\\face_age_original\\" + str(foldername)
        os.chdir(newdir)
        for file in glob.glob("*.png"):
            destfile = olddir + "\\face_age_add_age\\" + str(foldername) + "_" + str(file)
            shutil.move(file, destfile)
import os
import shutil
import utility

from pathConstants import *
from extensionsMapping import *

## move to the downloads folder

os.chdir(DESKTOP) 
print("We moved to directory " + os.getcwd())

folderToClean = os.getcwd()

for f in os.scandir(folderToClean):
    ext = utility.extractExtension(f.path)
    fileName = os.path.basename(f.path)

    if ext == 'noExt':
        print("skipped, still to manage")
    else:
        if ext in images_map:
            if not os.path.isdir(IMAGES):
                try:
                    os.mkdir(IMAGES)
                except:
                    print("Dunno")
            shutil.move(fileName, IMAGES)
        elif ext in pdf_map:
            if not os.path.isdir(PDF):
                try:
                    os.mkdir(PDF)
                except:
                    print("Dunno")
            shutil.move(fileName, PDF)
        elif ext in xml_map:
            if not os.path.isdir(XML):
                try:
                    os.mkdir(XML)
                except:
                    print("Dunno")
            shutil.move(fileName, XML)
        elif ext in text_map:
            if not os.path.isdir(TEXT):
                try:
                    os.mkdir(TEXT)
                except:
                    print("Dunno")
            shutil.move(fileName, TEXT)
        elif ext in excel_map:
            if not os.path.isdir(EXCEL):
                try:
                    os.mkdir(EXCEL)
                except:
                    print("Dunno")
            shutil.move(fileName, EXCEL)
        elif ext in video_map:
            if not os.path.isdir(VIDEO):
                try:
                    os.mkdir(VIDEO)
                except:
                    print("Dunno")
            shutil.move(fileName, VIDEO)
        elif ext in html_map:
            if not os.path.isdir(HTML):
                try:
                    os.mkdir(HTML)
                except:
                    print("Dunno")
            shutil.move(fileName, HTML)
        elif ext in js_map:
            if not os.path.isdir(JS):
                try:
                    os.mkdir(JS)
                except:
                    print("Dunno")
            shutil.move(fileName, JS)
        elif ext in json_map:
            if not os.path.isdir(JSON):
                try:
                    os.mkdir(JSON)
                except:
                    print("Dunno")
            shutil.move(fileName, JSON)
        elif ext in installer_map:
            if not os.path.isdir(INSTALLER):
                try:
                    os.mkdir(INSTALLER)
                except:
                    print("Dunno")
            shutil.move(fileName, INSTALLER)
        elif ext in zip_map:
            if not os.path.isdir(ZIP):
                try:
                    os.mkdir(ZIP)
                except:
                    print("Dunno")
            shutil.move(fileName, ZIP)
        elif ext in ppt_map:
            if not os.path.isdir(PPTX):
                try:
                    os.mkdir(PPTX)
                except:
                    print("Dunno")
            shutil.move(fileName, PPTX)

print("FERTIG!")
            


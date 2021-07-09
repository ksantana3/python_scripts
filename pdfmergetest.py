from os import listdir,mkdir,startfile
from os.path import isfile, join,exists
from PyPDF2 import PdfFileMerger
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
# Choosing the folder directory that contains the pdf files.
path_dir = filedialog.askdirectory()+"\\"

ulst = []

pdffiles = [f for f in listdir(path_dir) if isfile(join(path_dir, f)) and '.pdf' in f]
# Creating unique list of file names to the fifth character
for file in pdffiles:
    if file[:5] not in ulst:
        ulst.append(file[:5])  
# print(ulst)

for i in ulst:
    filemerger = PdfFileMerger()
    for file in listdir(path_dir):
        if file.endswith(".pdf") and file.startswith(i) and not file.endswith("_combined.pdf"):
            print(file)
            filemerger.append(path_dir+file)
    filemerger.write(path_dir+i+"_combined.pdf")
    filemerger.close()



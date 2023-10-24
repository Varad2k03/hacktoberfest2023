from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
folderPath = input("Enter the folder path: ")
fileType = input("Enter the file type: ").lower()
openFolder = os.listdir(folderPath)

for pdf in openFolder:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
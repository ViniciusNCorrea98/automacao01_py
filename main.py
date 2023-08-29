import PyPDF2
import os

merger = PyPDF2.PdfMerger()

list_files = os.listdir("arquivos")
list_files.sort()
print(list_files)

for file in list_files:
    if ".pdf" in file:
        merger.append(f'arquivos/{file}')

merger.write('PDF_Final.pdf')
print('Success!!')
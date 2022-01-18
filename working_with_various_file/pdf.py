import PyPDF2

with open('test.pdf' , 'rb') as pdf:
    read_pdf = PyPDF2.PdfFileReader(pdf)
    print('number of pages in test file is: ', read_pdf.numPages)
    
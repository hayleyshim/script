import PyPDF2
with open('test.pdf', 'rb') as pdf:
    read_pdf = PyPDF2.PdfFileReader(pdf)
    pdf_page = read_pdf.get_page(1)
    pdf_content = pdf_page.extractText()
    print(pdf_content)

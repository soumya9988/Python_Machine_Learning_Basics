import PyPDF2

with open('combinedminutes.pdf', 'rb') as pdf_object:
    pdf_reader = PyPDF2.PdfFileReader(pdf_object)
    print(pdf_reader.numPages)
    print(pdf_reader.isEncrypted)
    print(pdf_reader.getPage(0).extractText())

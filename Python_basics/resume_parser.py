from nltk import word_tokenize, pos_tag, sent_tokenize
import PyPDF2
import re
resume = []

with open('sample_resume.pdf', 'rb') as pdf_object:
    pdf_reader = PyPDF2.PdfFileReader(pdf_object)
    text = pdf_reader.getPage(0).extractText()


lines = [line.strip() for line in text.split('\n') if len(line) > 0]
lines = [word_tokenize(line) for line in lines]
lines = [pos_tag(line) for line in lines]
for line in lines:
    resume += line
print(resume)

#pattern = re.compile(r'\w+@[A-Z0-9]+\.[a-z]{2,4}', re.IGNORECASE)
#email_id = pattern.findall(resume)
#print(email_id)


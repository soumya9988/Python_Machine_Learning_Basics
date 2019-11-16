from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import PyPDF2

with open('sample_resume.pdf', 'rb') as pdf_object:
    pdf_reader = PyPDF2.PdfFileReader(pdf_object)
    text = pdf_reader.getPage(0).extractText()

sentences = sent_tokenize(text)
print(sentences)

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
words_req = [word for word in words if word not in stop_words]
print(words_req)


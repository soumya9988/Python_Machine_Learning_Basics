import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


def data_cleanup(sent):
    cleaned_data = []
    for item in sent:
        data = re.sub('[^A-Za-z]', ' ', item)
        data = data.lower().split()
        ps = PorterStemmer()
        data = [ps.stem(word) for word in data if not word in set(stopwords.words('english'))]
        sentence = ' '.join(data)
        cleaned_data.append(sentence)
    return cleaned_data


def vectorize(sentence):
    cv = CountVectorizer()
    X = cv.fit_transform(sentence).toarray()
    print(X)


def generate_bag_of_words(sent):
    clean_data = data_cleanup(sent)
    print(clean_data)
    vectorize(clean_data)


all_sentences = ["Joe waited for the train",
                "The train was late",
                "Mary and Samantha took the bus",
                "I looked for Mary and Samantha at the bus station",
                "Mary and Samantha arrived at the bus station early but waited until noon for the bus"]

generate_bag_of_words(all_sentences)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

def preprocess_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)

    filtered_data = [word for word in word_tokens if word.casefold() not in stop_words]

    return filtered_data

if __name__ == "__main__":
    file_path = "../data/jay_abraham_teachings.txt"
    preprocessed_data = preprocess_data(file_path)
    with open("../data/preprocessed_data.txt", "w") as file:
        file.write(' '.join(preprocessed_data))

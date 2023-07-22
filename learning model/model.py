import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


nltk.download('stopwords')

# print(stopwords.words('english'))

news_dataset = pd.read_excel('learning model\\news.xlsx')

# print(news_dataset)

news_dataset = news_dataset.fillna('')

news_dataset['Content'] = news_dataset["Title"] + ' ' + news_dataset["Text"]

# print(news_dataset['content'])

X = news_dataset.drop(columns='TorF', axis=1)
Y = news_dataset['TorF']

# print(X)
# print(Y)

port_stem = PorterStemmer()


def stemming(content):
    stemmed_content = re.sub('[^0-9a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [
        port_stem.stem(word)
        for word in stemmed_content
        if word not in stopwords.words('english')
    ]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content


news_dataset['content'] = news_dataset['content'].apply(stemming)

# print(news_dataset['content'])

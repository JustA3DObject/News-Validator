import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import joblib

nltk.download('stopwords')

# print(stopwords.words('english'))

news_dataset = pd.read_excel('news.xlsx')

# print(news_dataset)

news_dataset = news_dataset.fillna('')

news_dataset['content'] = news_dataset["Title"] + ' ' + news_dataset["Text"]

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

X = news_dataset['content'].values
Y = news_dataset['TorF'].values

# print(X)
# print(Y)

vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

# print(X)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=5)

model = SGDClassifier(loss='hinge', penalty='l2',
                      fit_intercept=True, shuffle=True)
model.partial_fit(X_train, Y_train, classes=np.unique(Y))

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

filename = "Completed_model.joblib"
joblib.dump(model, filename)

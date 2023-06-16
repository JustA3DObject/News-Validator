import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# print(stopwords.words('english'))

news_dataset = pd.read_excel('learning model\\news.xlsx')

# print(news_dataset)

news_dataset = news_dataset.fillna('')

news_dataset['Content'] = news_dataset["Title"] + ' ' + news_dataset["Text"]

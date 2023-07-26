from fastapi import FastApi
from pydantic import BaseModel
import pickle
import json
import re
from nltk.stem.porter import PorterStemmer

app = FastApi()

class model_input(BaseModel):

    News_Title : str
    News_Body : str

news_model = pickle.load(open("model.pkl", "rb"))

@app.post('/news_validator') #In point
def news_valid(input_parameters : model_input):

    input_data = input_parameters.json
    input_dictionary = json.loads(input_data)

    title = input_dictionary["News_Title"]
    body = input_dictionary["News_Body"]

    input_list = [title, body]

    input_string = "".join(input_list)

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

    processed_input = [stemming[input_string]]

    vectorizer = load(open('vectorizer.pkl', "rb"))

    input_string = vectorizer.transform(input_string)

    predictor = load(open("model.pkl", "rb"))

    if predictor.predict(input_stringw) == 1:
        return "The news is most certainly TRUE."
    else:
        return "The news is probably FAKE or has been manipulated. Fact checking is recommended."




    



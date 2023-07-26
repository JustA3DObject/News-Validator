from fastapi import FastApi
from pydantic import BaseModel
import pickle
import json

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
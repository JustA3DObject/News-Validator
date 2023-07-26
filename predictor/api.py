from fastapi import FastApi
from pydantic import BaseModel
import pickle
import json

app = FastApi()

class model_input(BaseModel):
    News_Title : str
    News_Body : str
    
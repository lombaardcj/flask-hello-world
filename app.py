from flask import Flask
from scraper import scrape
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    output = scrape()
    return print(json.dumps(output))

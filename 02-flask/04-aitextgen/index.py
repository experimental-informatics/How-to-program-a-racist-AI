
import openai
openai.api_key = "--"

def prompting(input_text):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=input_text,
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0.0,
      stop=['\n\n\n']
    )
    return response.choices[0].text

from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "hello"

import os 
import time

@app.route('/prompt/<input_text>', methods=['GET'])
def getText(input_text):
    input_text = input_text.replace("%20"," ")
    output = prompting(input_text)
    return '<html><body><h1>'+input_text+output+'</h1></body></html>' 


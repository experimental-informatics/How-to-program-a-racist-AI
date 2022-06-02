
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

@app.route("/")

@app.route("/hello_world")
def hello_world():
    reply = prompting("write a poem about flower")
    return str(reply)
import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def chat():
    return render_template("chatbox.html")

@app.route("/response", methods=["POST"])
def response():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": request.form["prompt"]},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    result = response["choices"][0]["message"]["content"]
    #result = response.choices[0].get("text")
    result = result.replace("\n", "<br>")
    return result

if __name__ == "__main__":
    app.run(debug=True)

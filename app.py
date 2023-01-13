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
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result = response.choices[0].text
    result = result.replace("\n", "<br>")
    return result


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, url_for, request
import spacy
from ner import SpacyDocument

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    rawtext = request.form['rawtext']
    doc = SpacyDocument(rawtext)
    messages = doc.get_entities_with_markup()
    return render_template('index.html', markup=messages)


if __name__ == '__main__':
    app.run(debug=True)

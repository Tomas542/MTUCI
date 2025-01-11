from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def trans():
    message = ""
    attention = ''
    if request.method == "POST":
        lang = request.form.get('lang')
        text = request.form.get('text')
        if text == '':
            attention = 'Incorrect text, try again'
        else:
            message = GoogleTranslator(source='auto', target=lang).translate(text)
        return render_template('trans.html', attention=attention, message=message)
    return render_template("trans.html")

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request, redirect
from day8_CeaserCypher import alphabet
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    webbrowser.open('http://0.0.0.0:5000/')


@app.route('/', methods=['GET', 'POST'])
def ceasar(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

@app.route('/result/<end_text>')
def show_result(end_text):
    return render_template('result.html', result=end_text)
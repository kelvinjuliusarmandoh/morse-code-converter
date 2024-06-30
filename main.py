from morse_converter import MorseCodeConverter
from flask import Flask, url_for, redirect, render_template
from flask_bootstrap import Bootstrap5
from forms import ConverterForm, InverterForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('form_secret_key')
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert/<command>", methods=['GET', 'POST'])
def converter(command):
    convert_form = ConverterForm()
    result = None
    if convert_form.validate_on_submit():
        converter = MorseCodeConverter(command=command, sentences=convert_form.text.data)
        result = converter.convert_to_x()
    return render_template('converter.html', convert_form=convert_form, result=result)

@app.route("/invert/<command>", methods=['GET', 'POST'])
def inverter(command):
    inverter_form = InverterForm()
    result = None
    if inverter_form.validate_on_submit():
        inverter = MorseCodeConverter(command=command, sentences=inverter_form.morse.data)
        result = inverter.convert_to_x()
    return render_template('inverter.html', inverter_form=inverter_form, result=result)

# print("Welcome to Morse Code Converter")
# user_command = input("Select your command (Convert/Invert) to Morse Code: ")
# user_text = input("Please insert your text: ")
#
# converter = MorseCodeConverter(command=user_command, sentences=user_text)
# converter.convert_to_x()

if __name__ == '__main__':
    app.run(debug=True)
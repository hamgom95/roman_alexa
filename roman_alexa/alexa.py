from flask import Blueprint

from flask_ask import Ask

bp_ask = Blueprint("alexa", __name__)

ask = Ask(bp_ask, "/")


@ask.launch
def new_game():

    welcome_msg = render_template("welcome")

    return question(welcome_msg)


@ask.intent("AMAZON.HelpIntent")
def help():
    return statement(render_template("help"))


@ask.intent("ConvertToRomanIntent", convert={"arabic": int})
def convert_to_roman(arabic):
    roman = space_chars(arab_to_roman(arabic))
    return statement(render_template("as_roman", roman=roman))


@ask.intent("ConvertToArabicIntent", convert={"roman": str})
def convert_to_arabic(roman):
    print(roman)
    arabic = roman_to_arab(roman)
    return statement(render_template("as_arabic", arabic=arabic))

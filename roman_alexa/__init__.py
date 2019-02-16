

import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


def create_app():
    logging.getLogger("flask_ask").setLevel(logging.DEBUG)

    app = Flask(__name__)

    from roman_alexa.alexa import bp_ask

    app.register_blueprint(bp_ask, url_prefix="/alexa")
    app.register_blueprint(bp_ask, url_prefix="/<lang_code>/alexa")

    @app.url_defaults
    def set_language_code(endpoint, values):
        if "lang_code" in values or not g.get("lang_code", None):
            return
        if app.url_map.is_endpoint_expecting(endpoint, "lang_code"):
            values["lang_code"] = g.lang_code

    @app.url_value_preprocessor
    def get_lang_code(endpoint, values):
        if values is not None:
            g.lang_code = values.pop("lang_code", None)

    return app


def main():
    app = create_app()
    app.run(debug=True)

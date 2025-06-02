#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel, _, ngettext

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)


@app.route('/')
def home():
    greeting = _("Hello, World!")

    message_count = 3
    messages = ngettext(
        "You have one message", 
        "You have %(num)d messages", 
        message_count
    ) % {'num': message_count}

    return render_template('index.html', greeting=greeting, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
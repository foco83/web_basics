# -*- coding: utf8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi primera app web"

if __name__ == "__main__":
    app.run()

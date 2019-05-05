"""
    File: Boot.py
    Author: Ethan Hunter
    Description: The main executable for Flask_Template
"""

CONFIGPATH = "./config/DefaultConfig.json"

from flask import Flask
from blueprints.defaultBlueprint.DefaultBlueprint import defaultBlueprint
from blueprints.jsonApiBlueprint.JsonApiBlueprint import jsonApiBlueprint
from blueprints.htmlBlueprint.HtmlBlueprint import htmlBlueprint

app = Flask("Flask_Template")

app.config.from_json(CONFIGPATH)

app.register_blueprint(htmlBlueprint, url_prefix = "/")
app.register_blueprint(defaultBlueprint, url_prefix = "/default")
app.register_blueprint(jsonApiBlueprint, url_prefix = "/api")

if (__name__ == '__main__'):
    app.run()

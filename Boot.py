"""
    File: Boot.py
    Author: Ethan Hunter
    Description: The main executable for Flask_Template
"""

from flask import Flask
from config.Config import Config
from blueprints.defaultBlueprint.DefaultBlueprint import defaultBlueprint
from blueprints.jsonApiBlueprint.JsonApiBlueprint import JsonApiBlueprint
from blueprints.htmlBlueprint.HtmlBlueprint import htmlBlueprint

conf = Config()
app = Flask("Flask_Template")

app.config.from_json(conf.CONFIGPATH)

jsonApiBlueprint = JsonApiBlueprint(conf.db_url).jsonApiBlueprint

app.register_blueprint(htmlBlueprint, url_prefix = "/")
app.register_blueprint(defaultBlueprint, url_prefix = "/default")
app.register_blueprint(jsonApiBlueprint, url_prefix = "/api")

if (__name__ == '__main__'):
    app.run()

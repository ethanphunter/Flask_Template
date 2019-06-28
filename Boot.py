"""
    File: Boot.py
    Author: Ethan Hunter
    Description: The main executable for Flask_Template
"""

from blueprints.defaultBlueprint.DefaultBlueprint import defaultBlueprint
from blueprints.htmlBlueprint.HtmlBlueprint import HtmlBlueprint
from blueprints.jsonApiBlueprint.JsonApiBlueprint import JsonApiBlueprint
from config.Config import Config

from flask import Flask

conf = Config()
app = Flask("Flask_Template")

app.config.from_json(conf.CONFIGPATH)

jsonApiBlueprint = JsonApiBlueprint(conf.db_url).jsonApiBlueprint
htmlBlueprint = HtmlBlueprint(conf.template_folder).htmlBlueprint

app.register_blueprint(htmlBlueprint, url_prefix = "/")
app.register_blueprint(defaultBlueprint, url_prefix = "/default")
app.register_blueprint(jsonApiBlueprint, url_prefix = "/api")

if (__name__ == '__main__'):
    app.run()

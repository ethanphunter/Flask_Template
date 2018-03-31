"""
    File: Boot.py
    Author: Ethan Hunter
    Description: The main executable for Flack_Template
"""

CONFIGPATH = "./config/DefaultConfig.json"

from flask import Flask
from blueprints.defaultBlueprint.DefaultBlueprint import defaultBlueprint

app = Flask("Flask_Template")

app.config.from_json(CONFIGPATH)

app.register_blueprint(defaultBlueprint, url_prefix = "/default")

if __name__ == '__main__':
    app.run()

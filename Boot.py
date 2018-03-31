"""
    File: Boot.py
    Author: Ethan Hunter
    Description: The main executable for Flack_Template
"""

CONFIGPATH = "./config/DefaultConfig.json"

from flask import Flask

app = Flask("Flask_Template")
app.config.from_json(CONFIGPATH)

if __name__ == '__main__':
    app.run()

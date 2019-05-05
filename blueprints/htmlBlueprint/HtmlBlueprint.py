from flask import Blueprint, render_template, session, request, redirect

htmlBlueprint = Blueprint("HtmlBlueprint", __name__, template_folder="templates")

@htmlBlueprint.route("/index", methods = ["GET"])
def index():
    return render_template("Index.html")

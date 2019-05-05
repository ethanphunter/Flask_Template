from flask import Blueprint, render_template, session, request, redirect

htmlBlueprint = Blueprint("HtmlBlueprint", __name__, template_folder="templates")

@htmlBlueprint.route("/index", methods = ["GET"])
def index():
    return render_template("Index.html")

@htmlBlueprint.route("/param")
def param():
    p = request.args.get('p')
    return render_template("Param.html", parameter = p)

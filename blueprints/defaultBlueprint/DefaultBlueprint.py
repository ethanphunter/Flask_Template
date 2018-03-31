from flask import Blueprint

defaultBlueprint = Blueprint("Default_Blueprint", __name__)

@defaultBlueprint.route("/ping", methods = ["GET"])
def ping():
    return "pong"

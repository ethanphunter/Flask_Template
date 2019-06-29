from flask import Blueprint, render_template, session, request, redirect

class HtmlBlueprint(object):
    """ A simple example of how to use html templates """

    def __init__(self, template_folder):
        super(HtmlBlueprint, self).__init__()
        htmlBlueprint = Blueprint("HtmlBlueprint", __name__, template_folder = template_folder)

        @htmlBlueprint.route("/index", methods = ["GET"])
        def index():
            return render_template("Index.html")

        @htmlBlueprint.route("/param")
        def param():
            p = request.args.get('p')
            return render_template("Param.html", parameter = p)

        self.htmlBlueprint = htmlBlueprint

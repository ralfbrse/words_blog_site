from flask import Blueprint, render_template

# views : Instance of Blueprint
views = Blueprint("views", __name__)

# create routes for views blueprint
# template can be reached with /home or /
@views.route("/")
@views.route("/home")
# render_template() : render template with given name of file
def home():
    return render_template("home.html", name="Tim")

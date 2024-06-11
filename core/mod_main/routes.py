from flask import redirect, Blueprint, render_template
mod_main = Blueprint('main', __name__, template_folder='./../templates')


@mod_main.route('/', methods=["GET", "POST"])
def redirect_to_landing():
    return redirect("/home")


@mod_main.route('/home', methods=['GET', 'POST'])
def landing_page():
    return render_template("src/home.html")


@mod_main.route('/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template("src/contact.html")


@mod_main.route('/experience', methods=['GET', 'POST'])
def experience_page():
    return render_template("src/experience.html")

from flask import Flask, render_template
from .config import BaseConfig

# For import *
__all__ = ['app']


###########################################################################
# INITIALIZE MAIN APPLICATION

app = Flask(
    BaseConfig.PROJECT,
    subdomain_matching=True,
    template_folder='./core/templates',
    instance_relative_config=True
)

app.config.from_object(BaseConfig)


###########################################################################
# REGISTER BLUEPRINTS

from core.mod_main.routes import mod_main

app.register_blueprint(mod_main)


###########################################################################
# CONFIGURE HANDLERS

@app.errorhandler(404)
def invalid_route(e):
    return render_template("error/404.html")


# ------------------------------ END OF FILE ------------------------------

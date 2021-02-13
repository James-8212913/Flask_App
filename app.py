import markdown, pygments
from flask import Flask, render_template, render_template_string
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()


app = Flask(__name__)

## Nav Bar Elements
topbar = Navbar('',
    View('Home', 'index'),
)

nav.register_element('top', topbar)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

nav.init_app(app)

import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages

# Some configuration, ensures
# 1. Pages are loaded on request.
# 2. File name extension for pages is Markdown.
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

# URL Routing - Home Page
@app.route("/")
def home():
    return render_template("base.html")


@app.route('/articles')
def articles():
    return render_template('articles.html', pages=pages)

@app.route('/references')
def references():
    return render_template('base.html')

# URL Routing - Flat Pages
# Retrieves the page path and renders the template with metadata if requested
@app.route("/articles/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


# Main Function, Runs at http://0.0.0.0:8000
if __name__ == "__main__":
    app.run(port=8000)

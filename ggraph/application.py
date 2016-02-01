import io
import mimetypes
import logging

# flask import
from flask import Flask, send_file

# graphviz import
from graphviz import Source
from graphviz.files import ENGINES, FORMATS

# markdown import
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

app = Flask(__name__)

@app.before_first_request
def setup_logging():
    if not app.debug:
        # production mode
        app.logger.addHandler(logging.SysLogHandler())
        app.logger.setLevel(logging.INFO)
    else:
        # debug mode
        app.logger.addHandler(logging.StreamHandler(sys.stderr))
        app.logger.setLevel(logging.DEBUG)

@app.route('/<engine>/<outformat>/<graphviz_code>')
def generate(engine, outformat, graphviz_code):
    src = Source(graphviz_code, engine=engine, format=outformat)

    fb = io.BytesIO(src.pipe())

    app.logger.debug(fb.getvalue())
    app.logger.debug(outformat)

    return send_file(fb, mimetype=mimetypes.types_map['.'+outformat])

@app.route('/engine')
def get_list_of_engine():
    return ", ".join(ENGINES)

@app.route('/format')
def get_format():
    return ", ".join(FORMATS)

@app.route('/')
def index():
    readme = open("Readme.md", mode="r").read()
    return markdown.markdown(readme, output_format="html5", extension=[
        markdown.extensions.codehilite
    ])

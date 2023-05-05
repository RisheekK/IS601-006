from flask import Blueprint, request, render_template
hello = Blueprint('hello', __name__, url_prefix='/',template_folder='templates')


@hello.route('/')
def index():
    # rr284 21 april 2023
    name = request.args.get('name', 'World')
    return render_template("index.html", name=name)
# see home.py in routes for more details
from flask import Blueprint, render_template

# url_prefix puts /dashboard before all of the given routes in this blueprint
# The routes thus become /dashboard and /dashboard/edit/<id> when registered with the app.
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

# gets id of the post from the url
@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')
from flask import (
    render_template, 
    Blueprint
)

from app.models import Book

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def index():
    books = Book.query.all()

    return render_template(
        'index.html',
        books = books
    )

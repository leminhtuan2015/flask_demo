from flask import Blueprint, render_template

products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')

@products_bp.route('/')
def index():
    return render_template('products/index.html', products=["product 1", "product 2"])

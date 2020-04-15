from flask import Flask, render_template
from products.products import products_bp

app = Flask(__name__)

app.register_blueprint(products_bp, url_prefix='/products')

print("__name__: " + __name__)

@app.route('/')
def index():
    return render_template('index.html', name = "Tuan a")

if __name__ == '__main__':
   app.run(debug = True) # debug = True, auto recompile code when save changed
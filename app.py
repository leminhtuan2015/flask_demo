from flask import Flask, render_template

from products.productController import products_bp
from temperature.temperatureController import temperrature_bp

app = Flask(__name__)

app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(temperrature_bp, url_prefix='/temperature')

print("__name__: " + __name__)

@app.route('/')
def index():
    return render_template('index.html', name = "Tuan a")

if __name__ == '__main__':
   app.run(debug = True) # debug = True, auto recompile code when save changed
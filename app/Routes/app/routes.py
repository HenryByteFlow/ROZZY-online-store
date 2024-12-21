from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('index.html', title="ROZZY Store")

@main.route("/product/<int:product_id>")
def product(product_id):
    return render_template('product.html', title="Product Details")

@main.route("/cart")
def cart():
    return render_template('cart.html', title="Your Cart")

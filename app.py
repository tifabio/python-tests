from flask import Flask, jsonify, request, render_template
from shop_cart import ShopCart


app = Flask(__name__)
cart = ShopCart()


@app.route('/cart', methods=['GET'])
def get():
    return jsonify(cart.getProducts())

@app.route('/cart/product', methods=['POST'])
def post():
    product = request.get_json()
    cart.addProduct(product)
    return jsonify(), 201

@app.route('/cart/product/<id>', methods=['DELETE'])
def delete(id):
    cart.delProduct(id)
    return jsonify()


@app.route('/')
def index():
    return render_template('index.html', products = [
        {
            'id': '1',
            'title': 'Book',
            'price': 15
        },
        {
            'id': '2',
            'title': 'Mouse',
            'price': 70
        }
    ])


if __name__ == '__main__':
    app.run(debug=True)
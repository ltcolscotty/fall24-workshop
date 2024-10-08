from flask import flask, request, jsonify

app = flask(__name__)

# Mock data for demonstration purposes

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 10.99,
        "quantity": 50
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 15.99,
        "quantity": 30
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 20.99,
        "quantity": 20
    }
]



@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404
    

@app.route("/products", methods=["POST"])
def add_product():
    new_product = request.get_json()
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201



@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        updated_product = request.get_json()
        product.update(updated_product)
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        products.remove(product)
        return jsonify({"message": "Product deleted successfully"})
    else:
        return jsonify({"error": "Product not found"}), 404
    
@app.route("/", methods=["GET", "POST, PUT", "DELETE"])
def index():    
    return jsonify({"message": "Welcome to the Product API! Use the /products endpoint to manage products."})


if __name__ == "__main__":
    app.run(debug=True)

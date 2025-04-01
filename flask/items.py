from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "Description of Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description of Item 2"},
]

@app.route("/")
def home():
    return "Welcome to the Item API!"

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        updated_item = request.get_json()
        item.update(updated_item)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

@app.route("/items/search", methods=["GET"])
def search_items():
    query = request.args.get("query", "")
    filtered_items = [item for item in items if query.lower() in item["name"].lower()]
    return jsonify(filtered_items)

if __name__ == "__main__":
    app.run(debug=True)
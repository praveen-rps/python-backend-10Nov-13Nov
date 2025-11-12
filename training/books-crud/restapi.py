from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# In-memory data store (for demonstration purposes)
items = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"}
]

# Parser to handle request data (for POST and PUT)
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the item', required=True)

class Item(Resource):
    def get(self, item_id):
        # Get a single item by its ID
        item = next((i for i in items if i["id"] == item_id), None)
        if item:
            return item, 200
        return {"message": "Item not found"}, 404

    def delete(self, item_id):
        # Delete an item by its ID
        global items
        items = [item for item in items if item["id"] != item_id]
        return {"message": "Item deleted"}, 200

    def put(self, item_id):
        # Update an existing item
        data = parser.parse_args()  # Retrieve data from the request
        item = next((i for i in items if i["id"] == item_id), None)
        if item:
            item['name'] = data['name']
            return item, 200
        return {"message": "Item not found"}, 404

class ItemList(Resource):
    def get(self):
        # Get all items
        return {"items": items}, 200

    def post(self):
        # Create a new item
        data = parser.parse_args()
        new_id = max([item["id"] for item in items], default=0) + 1
        new_item = {"id": new_id, "name": data['name']}
        items.append(new_item)
        return new_item, 201


# Add routes to the API
api.add_resource(ItemList, '/items')  # /items for GET and POST
api.add_resource(Item, '/items/<int:item_id>')  # /items/<id> for GET, PUT, DELETE

if __name__ == '__main__':
    app.run(debug=True)

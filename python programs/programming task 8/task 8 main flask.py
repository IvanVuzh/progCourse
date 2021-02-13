from OrderFile import Order
from CollectionFile import Collection
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRING_REGULAR'] = True
collection = Collection()
file_name = "task8data.json"
collection.read_from_file(file_name)
collection.print()

fields_list = ['id',
               'order_status',
               'amount',
               'discount',
               'order_date',
               'shipped_date',
               'customer_email']
error_messages = ["wrong id entered",
                  "wrong order status entered",
                  "wrong amount entered",
                  "wrong discount entered",
                  "wrong order date entered",
                  "wrong shipped date entered",
                  "wrong customer email entered"]


@app.route('/orders/', methods=['POST'])
def create_new_order():
    init_dict = dict()
    iter = 0
    error_list = []
    for i in fields_list:
        if i not in request.args:
            error_list.append(error_messages[iter])
            return jsonify({"status": 401, "message": "missing some data"})
        else:
            init_dict[i] = request.args[i]
        iter += 1
    new_order = Order(init_dict)
    if not collection.get_by_id(new_order.id):
        if new_order.id == 0:
            error_message = ''
            for error in error_list:
                error_message += error + "\n"
            return jsonify({"status": 400, "message": error_message})
        else:
            collection.add_order(new_order)
            collection.rewriting_to_file(file_name)
            return jsonify({"status": 201, "message": "order has been successfully added"})
    else:
        return jsonify({"status": 400, "message": "Order with such id already exist"})


@app.route('/orders/<given_id>/', methods=['DELETE'])
def delete_by_id(given_id):
    if collection.deleter(given_id):
        collection.rewriting_to_file(file_name)
        return jsonify({"status": 200, "message": "Order has been successfully deleted"})
    else:
        return jsonify({"status": 404, "message": "No customer with such id"})


@app.route('/orders/<given_id>/', methods=['GET'])
def get_one(given_id):
    res = collection.get_by_id(int(given_id))
    if res is False:
        return jsonify({"status": 404, "message": "No customer with such id"})
    else:
        return jsonify(res.order_to_dict())


@app.route('/orders/', methods=['GET'])
def orders():
    if collection.get_len() > 0:
        if 's' in request.args:
            find = request.args['s']
            res = collection.search(find)
            return jsonify(res)
        elif 'sort_by' in request.args and 'sort_type' in request.args:
            res = collection.sort(request.args['sort_by'], request.args['sort_type'])
        else:
            res = collection.return_list_of_dicts()
        collection.rewriting_to_file(file_name)
        return jsonify(res)  # json.dumps(collection.return_list_of_dicts(), indent=4)
    else:
        return "there are no orders"


@app.route('/orders/<given_id>/', methods=['PUT'])
def update_order(given_id):
    present = collection.get_by_id(given_id)
    if present is False:
        return jsonify({"status": 404, "message": "No customer with such id"})
    else:
        for data in request.args:
            if data not in fields_list:
                return jsonify({"status": 401, "message": "missing some data"})
        res = collection.edit_all_fields(given_id, request.args)
        collection.rewriting_to_file(file_name)
        return jsonify(res)


if __name__ == '__main__':
    collection = Collection()
    collection.read_from_file("task8data.json")
    app.run()

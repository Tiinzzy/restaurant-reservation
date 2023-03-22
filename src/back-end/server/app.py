from flask import Flask, request, jsonify
from business.user import User
from business.menu_item import MenuItem
from business.seating_table import SeatingTable

app = Flask(__name__)


@app.route('/create-new-user-account', methods=["POST"])
def create_new_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    birthday = request.json['birthday']

    user = User()
    user.set_name(name)
    user.set_email(email)
    user.set_password(password)
    user.set_birthday(birthday)

    result = user.add()
    return jsonify(result)


@app.route('/update-user-account', methods=["POST"])
def update_user_account():
    email = request.json['email']
    password = request.json['password']

    user = User()
    is_a_match = user.password_matches(email)
    if is_a_match['password'] == password:
        User.load(is_a_match['id'])

    return True


@app.route('/get-menu-items-categories', methods=["POST"])
def get_menu_items_categories():
    categories = MenuItem.get_categories()
    return jsonify(categories)


@app.route('/add-menu-item', methods=["POST"])
def add_menu_item():
    name = request.json['name']
    category = request.json['category']
    price = request.json['price']
    description = request.json['description']

    menu_item = MenuItem()
    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.add()
    return jsonify(result)


@app.route('/select-all-menu-items', methods=["POST"])
def select_all_menu_items():
    menu_items = MenuItem.select_all_menu_items()
    return jsonify(menu_items)


@app.route('/delete-menu-item', methods=["POST"])
def delete_menu_item():
    menu_item_id = request.json['id']

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    result = menu_item.delete()
    return jsonify(result)


@app.route('/load-menu-item', methods=["POST"])
def load_menu_item():
    menu_item_id = request.json['id']

    menu_item = MenuItem()
    result = menu_item.load(menu_item_id)
    return jsonify(result)


@app.route('/update-menu-item', methods=["POST"])
def update_menu_item():
    menu_item_id = request.json['id']
    name = request.json['name']
    category = request.json['category']
    price = request.json['price']
    description = request.json['description']

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.update()
    return jsonify(result)


@app.route('/add-seating-table', methods=["POST"])
def add_seating_table():
    seat_count = request.json['seat_count']
    available = request.json['available']

    seating_table = SeatingTable()
    seating_table.set_seat_count(seat_count)
    seating_table.set_available(available)

    result = seating_table.add()
    return jsonify(result)


@app.route('/select-all-available-seats', methods=["POST"])
def select_available_seats():
    seat_count = request.json['seat_count']

    result = SeatingTable.select_available_seats(int(seat_count))
    return jsonify(result)


@app.route('/get-all-seating-tables', methods=["POST"])
def get_all_seating_tables():
    result = SeatingTable.select_all_seating_tables()
    return jsonify(result)


@app.route('/load-seating-table', methods=["POST"])
def load_a_seating_table():
    seat_id = request.json['id']
    table = SeatingTable()
    result = table.load(seat_id)
    return jsonify(result)


@app.route('/update-seating-table', methods=["POST"])
def update_seating_table():
    seat_id = request.json['id']
    available = request.json['available']

    table = SeatingTable()
    table.load(seat_id)
    table.set_available(available)

    result = table.update()
    return jsonify(result)

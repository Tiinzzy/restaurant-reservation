from flask import Flask, request, jsonify
from business.user import User
from business.menu_item import MenuItem

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

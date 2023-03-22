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

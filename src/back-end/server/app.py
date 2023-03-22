from flask import Flask, request, jsonify
from business.user import User

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

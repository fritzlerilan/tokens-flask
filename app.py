from flask import Flask, request, Response, jsonify
from cryptography.fernet import Fernet

TOKEN = 'token'
USERNAME = 'username'
PASSWORD = 'password'
TTL = 40  # Seconds Time to Leave

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.args.get(USERNAME) or request.form.get(USERNAME)
    pwd = request.args.get(PASSWORD) or request.form.get(PASSWORD)
    if user and pwd:
        if user == 'admin' and pwd == 'admin':
            response = Response()
            response.headers[TOKEN] = '123456789'  # token via headers
            response.status_code = 200
            return response, 200
        else:
            return "Username or password incorrect", 401
    else:
        return "Missing login args", 400


@app.route("/secret-things", methods=["GET"])
def showSecretThings():
    token_info = request.get_json() or request.form
    token = token_info.get(TOKEN)
    if token:
        if token == '123456789':
            return jsonify({
                "message": "This was just a joke. Thank you for autheticating :)"
            }), 200
    return "", 401


if __name__ == '__main__':
    app.run(debug=True)

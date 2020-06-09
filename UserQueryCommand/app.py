from flask import Flask, jsonify, request

from Services.UserService import UserService

app = Flask(__name__)


@app.route('/user-details/<int:userid>', methods=['GET'])
def getUserDetails(userid):
    userService = UserService()
    return jsonify(userService.getUserDetails(userid))


@app.route('/user-details', methods=['POST'])
def submitUserDetails():
    userService = UserService()

    jsonRequest = request.get_json()
    return jsonify(userService.submitUserDetails(jsonRequest))


@app.route('/validate-user', methods=['POST'])
def validateUser():
    username_password = request.get_json(force=True)
    userService = UserService()
    return jsonify(userService.validateUsernamePassword(username_password))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8004)

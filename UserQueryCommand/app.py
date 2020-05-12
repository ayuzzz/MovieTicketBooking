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


if __name__ == '__main__':
    app.run()

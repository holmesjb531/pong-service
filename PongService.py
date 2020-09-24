import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPDigestAuth, HTTPAuth
import requests


app = Flask(__name__)
auth = HTTPAuth()



usernamePassword = {
    'vcu': 'rams'
}
#
# @app.errorhandler(404)
# def page_not_found(e):
#     jsonify({'message': 'Page Not Found'}), 404
#
#
# @app.errorhandler(500)
# def internal_server_error():
#     jsonify({'message': 'Something went wrong :('}), 500


@auth.get_password
def get_password(username):
    if username in usernamePassword:
        return usernamePassword.get(username)
    return None

@app.route('/pong', methods=['GET'])
@auth.login_required
def pong_service():
    return jsonify({'msg': 'Working!'}), 200


if __name__ == '__main__':
    app.run()

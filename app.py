from flask import Flask, request,jsonify

app = Flask(__name__)


@app.route('/')
def details():
    return """
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999<br>
    """


@app.route('/welcome')
def welcome():
    return "<h1> Welcome to ABC Corporation</h1>"

@app.route('/postman_action', methods=['POST'])
def hello_world():
    mess = request.json['message']
    return jsonify(mess)


if __name__ == '__main__':
    app.run( debug = True)
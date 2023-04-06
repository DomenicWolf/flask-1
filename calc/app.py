# Put your app in here.
from flask import Flask
from operations import add
from flask import request
from operations import sub
from operations import mult
from operations import div

app = Flask(__name__)

@app.route('/add')
def search_add():
    a = request.args['a']
    b = request.args['b']
    return f"{add(int(a),int(b))}"

@app.route('/sub')
def search_sub():
    print(request.args['a'])
    a = request.args['a']
    b = request.args['b']
    return f"{sub(int(a),int(b))}"

@app.route('/mult')
def search_mult():
    a = request.args['a']
    b = request.args['b']
    return f"{mult(int(a),int(b))}"

@app.route('/div')
def search_div():
    a = request.args['a']
    b = request.args['b']
    return f"{div(int(a),int(b))}"

functions = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}
@app.route('/math/<oper>')
def all(oper):
    a = request.args['a']
    b = request.args['b']
    return f"{functions[oper](int(a),int(b))}"
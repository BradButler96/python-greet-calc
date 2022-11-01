from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add', methods=["GET"])
def sum():
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)
    sum = add(int_a,int_b)
    return f'<p>{sum}</p>'

@app.route('/sub', methods=["GET"])
def diff():
    """Substract b from a."""
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)
    diff = sub(int_a,int_b)
    return f'<p>{diff}</p>'

@app.route('/mult', methods=["GET"])
def prod():
    """Multiply a and b."""
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)
    prod = mult(int_a,int_b)
    return f'<p>{prod}</p>'

@app.route('/div', methods=["GET"])
def quot():
    """Divide a by b."""
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)
    quot = div(int_a,int_b)
    return f'<p>{quot}</p>'

@app.route('/math/<func>', methods=["GET"])
def all(func):
    a = request.args.get('a')
    b = request.args.get('b')
    int_a = int(a)
    int_b = int(b)
    functions = {
        'add': add(int_a,int_b),
        'sub': sub(int_a,int_b),
        'mult': mult(int_a,int_b),
        'div': div(int_a,int_b)
    }
    function = functions.get(func, "Func not found")
    return f'<p>{function}</p>'

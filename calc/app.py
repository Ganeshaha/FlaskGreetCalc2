# Put your app in here.
from flask import Flask, request
import operations

app = Flask("calc")

@app.route("/add")
def add_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{operations.add(a,b)}"

@app.route("/sub")
def sub_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{operations.sub(a,b)}"

@app.route("/div")
def div_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{operations.div(a,b)}"

@app.route("/mult")
def mult_func():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{operations.mult(a,b)}"

@app.route("/math/<operation>")
def all_operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    op_dict = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div
    }
    return f"{op_dict[operation](a,b)}"
from flask import Flask, Response, redirect, url_for

app = Flask(__name__)
ToDo = {}


@app.route('/todo/show')
def todo_show():
    return ToDo


@app.route('/todo/add/<name>/<task>')
def todo_add(name, task):
    ToDo[name] = task
    return ToDo


@app.route('/todo/clear')
def todo_clear():
    ToDo.clear()
    return ToDo


@app.route('/todo/remove/<name>')
def todo_remove(name):
    ToDo.pop(name)
    return ToDo


if __name__ == "__main__":
    app.run(debug=True)

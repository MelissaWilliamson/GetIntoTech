from flask import Flask, Response, request, url_for, redirect

app = Flask(__name__)
fruits = []

@app.route('/')
def hello_from_flask():
    return "Hello from flask!"

@app.route('/get/text')
def get_tex():
    return Response('Hello from flask using an explicit response option', mimetype='text/plain')

@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response('You posted this data to the Flask app:' + data_sent, mimetype='text/plain')

@app.route('/dynamic/<word>')
def home(word):
    return word

@app.route('/square/<int:number>')
def square(number):
    square = number ** 2
    line = 'Your number squared is' + ' ' + str(square)
    return line

@app.route('/numbers/<int:num1>/<int:num2>')
def sum(num1, num2):
    sum = num1 + num2
    line = "your sum is" + " " + str(sum)
    return line

@app.route('/home/<name>')
def say_hello(name):
    return '''
    <html>
    <head>
    <title> sample - flask routes </title>
    </head>
    <body>
    <h1>Name page</h1>
    <p> Hello {} </p>

    </body>
    </html>
    '''.format(name)

@app.route('/fruits/add/<fruit>')
def AddFruit(fruit):
    fruits.append(fruit)
    return fruits

@app.route('/fruits/remove/<fruit>')
def RemoveFruit(fruit):
    fruits.remove(fruit)
    return fruits


@app.route('/login/<name>')
def login(username):
    url = url_for('profile', username=username)
    return """

    <html>
    <head>
    <title>Login Page {}</title>
    </head>
    <body>
    <h1>Login Page: {}</h1>
    <p>click link</p>
    <a href="{}">Login</a>
    </body>
    </html>
    """.format(username, username, url)


@app.route('/home/userprofile/<username>')
def profile(username):
    url = url_for('profile', username=username)
    return """
    <html>
    <head>
    <title>Welcome to your profile {}</title>
    </head>
    <body>
    <h1>User Profile: {}</h1>
    </body>
    </html>
    """.format(username, username)


@app.route('/home/external')
def external():
    return redirect('https://www.sky.com/')


if __name__ == '__main__' :
    app.run(debug=True)
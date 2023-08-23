from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def home():
    return render_template("home.html", title="home")

@app.route('/fruits')
def fruits():
    fruit = ['apple', 'orange', 'mango']
    return render_template("fruits.html", title="Fruits", fruits=fruit)

@app.route('/favourites')
def favourites():
    locations = ['Thailand', 'New York', 'Florida']
    return render_template("favourites.html", title="Favourite Locations", favourites=locations)

@app.route('/about')
def about():
    me = ['Name is Melissa', 'Worked at Sky for 4 years', 'I enjoy travelling']
    return render_template("about.html", title="About Me", about=me)

if __name__ == "__main__":
    app.run(debug=True)
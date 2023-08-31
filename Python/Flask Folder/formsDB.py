from flask import *
import os
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234XCVB'

def Connection():
    #Connection parameters
    server = 'localhost'
    db = 'Sakila'
    uid = 'newuser'
    pwd = 'password'

    #connection object

    conn = pymysql.connect(host=server, user=uid, password=pwd, database=db)

    conn.autocommit(True)

    return conn

@app.route('/country', methods=['GET','POST'])
def AddCountry():
    if request.method=='POST':
        country = request.form['country'] ##this part refers to the value of name in the country html file

        conn = Connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO country(country) VALUES('"+country+"')")

        return "Country saved successfully"

    return render_template("country.html")

@app.route('/actor', methods=['GET','POST'])
def Actor():
    if request.method=='POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]

        conn = Connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO actor(first_name, last_name) VALUES('" + firstname+ "', '" +lastname + "')")
        return "Actor saved successfully"

    return render_template("actor.html")

@app.route('/customers')
def getCusotmers():

        customers=[]
        conn = Connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMER")

        for row in cursor.fetchall():
            customers.append({"customer_id":row[0],"first_name":row[2], "last_name":row[3], "email_address":row[4]})
        conn.close()

        return render_template("customer.html", customers=customers)

@app.route('/Delete/<lang>')
def DeleteLanguage(lang):
    conn = Connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM language WHERE name ='" +lang +"'")

    return ("Successfully deleted"+lang)

if __name__=='__main__':
    app.run(debug=True)




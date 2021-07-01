from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-2.caomyyms75ok.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'suriya'
app.config['MYSQL_PASSWORD'] = 'suriya123'
app.config['MYSQL_DB'] ='regform'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        age = details['age']
        email = details['email']
        phone = details['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdata(name, age, email, phone) VALUES (%s, %s, %s, %s)", (name, age, email, phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/users')
def users():
    cur =mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM userdata")
    if resultValue > 0:
        usersDetails = cur.fetchall()

        return render_template('users.html',usersDetails=usersDetails)

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=80)

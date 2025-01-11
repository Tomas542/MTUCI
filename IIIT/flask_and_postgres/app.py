import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="123456789",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login1.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            warning = ''
            username = request.form.get('username')
            password = request.form.get('password')
            if password == '' and username == '':
                warning = 'You have not entered username and password'
            elif password == '':
                warning = 'You have not entered password'
            elif username == '':
                warning = 'You have not entered username'
            else:
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
                           (str(username), str(password)))
                records = list(cursor.fetchall())

                if not records:
                    warning = 'Sorry, there is no such user in DataBase'
                    return render_template('account.html', warning=warning)

                else:
                    return render_template('account.html', full_name=records[0][1], warning=warning)

            return render_template('account.html', warning=warning)

        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login1.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        warning = ''

        if name == '' or login == '' or password == '':
            warning = 'Please, fill every feild'
        else:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                           (str(name), str(login), str(password)))
            conn.commit()

            return redirect('/login/')

    return render_template('registration.html', warning=warning)


if __name__ == "__main__":
    app.run()
#code for webpage to register/de-register keys, send data to server and display response
#from server

from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        URL = "https://192.168.178.62:4997/register"
        print(request.form['action'])
        PARAMS = {"username": request.form['Uname'], "password": request.form['Pass'], "action":request.form['action'], "card_no":request.form['card'], "door_no":request.form['door']}
        r = requests.get(url=URL, params=PARAMS, verify=False)
        print(r.text)
        if r.text == 'Invalid credentials':
            error = 'Invalid Credentials. Please try again.'
        else:
            error = r.text
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(host='192.168.178.62',port=4991, ssl_context=(r'C:\Users\*****\cert.pem',r'C:\Users\****\key.pem'))

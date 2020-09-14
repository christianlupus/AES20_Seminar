#server program

from flask import Flask
from flask import request
import mysql.connector

app = Flask(__name__)
app.config["DEBUG"] = True

#connect to db running on server
db = mysql.connector.connect(user='root', password='RFID',
                              host='127.0.0.1',
                              database='rfid_data')

#code to validate keys
@app.route("/access",methods=['GET','POST'])
def access():
    cursor = db.cursor()
    if request.method == 'GET':
        rfid_tag = request.args.get("tag_id")
        door_id = request.args.get("door")
        sql = "SELECT ID FROM rfid WHERE `Card number` = "+rfid_tag+ " AND Door ='"+door_id+"'"
        print(sql)
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        if records:
            return "Access Granted"
        else:
            return "Access Denied"
    else:
        return "not granted"
    cursor.close()

#code to authenticate admin and register/de-register keys.
@app.route("/register",methods=['GET','POST'])
def register():
    cursor = db.cursor()
    if request.method == 'GET':
        username = request.args.get("username")
        password = request.args.get("password")
        action = request.args.get("action")
        rfid_no = request.args.get("card_no")
        door = request.args.get("door_no")
        ad_sql = "SELECT Id FROM user WHERE username = '" + username + "' AND password ='" + password + "'"
        cursor.execute(ad_sql)
        admin_records = cursor.fetchall()
        print('ad',admin_records)
        print('act',action)
        if admin_records:
            sql = "SELECT ID FROM rfid WHERE `Card number` = "+rfid_no+ " AND Door ='"+door+"'"
            cursor.execute(sql)
            records = cursor.fetchall()
            print(records)
            if (action == 'Insert' and records):
                return "Data exists"
            elif (action == 'Insert'):
                sql = "INSERT INTO rfid (`Card number`, Door) VALUES (%s, %s)"
                val = (rfid_no,door )
                cursor.execute(sql, val)
                db.commit()
                return "Data inserted"
            elif (action == 'Delete' and records):
                sql = "DELETE FROM rfid WHERE `Card number` = " + rfid_no + " AND Door ='" + door + "'"
                cursor.execute(sql)
                db.commit()
                return "Data deleted"
            elif (action == 'Delete'):
                return 'No existing data found'
        else:
            return "Invalid credentials"
    else:
        return "not granted"

if __name__ == "__main__":
    app.run(host='192.168.178.62',port=4997, ssl_context=(r'C:\Users\*******\cert.pem',r'C:\Users\******\key.pem'))


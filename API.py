# create a route
from flask import *
import pymysql

# create app
app = Flask(__name__)
# connection
con = pymysql.connect(host="keithwarui50.mysql.pythonanywhere-services.com", user="keithwarui50",
                      password="VANAlito1997", database="keithwarui50$default")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    #     json format
    # this is a file format
    json = request.json
    name = json['name']
    email = json['email']
    phone = json['phone']
    password = json['password']
    confirm_password = json['confirm_password']
#     validation checks
    if " " not in name:
        response=jsonify({"message":"Name must be two words"})
        response.status_code=401
        return response
    elif "@" not in email:
        response=jsonify({"message":"Kindly fill in a valid email address"})
        response.status_code = 402
        return response
    elif "254" not in phone:
        return=jsonify({"message":"Phone must start with 254"})
        response.status_code = 403
        return response
    elif len(phone) !=12:
        return=jsonify({"message": "Enter a valid phone number"})
        response.status_code = 404
        return response
    elif password != confirm_password:
        return=jsonify({"message","Password does not match Confirm Password"})
        response.status_code = 405
        return response
    else:
        con = pymysql.connect(host="keithwarui50.mysql.pythonanywhere-services.com", user="keithwarui50",
                              password="VANAlito1997", database="keithwarui50$default")
        sql='insert into signup (name,email,phone,password,confirm_password) values(%s,%s,%s,%s,%s)'
        cursor=con.cursor()
        try:
            cursor.execute(sql,(name,email,phone,password,confirm_password))
            con.commit()
            response=jsonify({"message":"Signup successful"})
            response.status_code=200
            return response
        except:
            response=jsonify({"message":"Ooops, something went wrong, will be with you in a minute"})
            response.status_code=500

# Signup API

@app.route("/signin",methods=['POST'])
def signin():
    json=request.json
    email=json['email']
    password=json['password']
    # connection
    con = pymysql.connect(host="keithwarui50.mysql.pythonanywhere-services.com", user="keithwarui50",
                          password="VANAlito1997", database="keithwarui50$default")
    try:
        cursor=con.cursor()
        sql="select * from signup where email=%s and password=%s"
        cursor.execute(sql,(email,password))
    #     check if theres a user with the credentials
        if cursor.rowcount == 0:
            response = jsonify({"message":"There is no user with above details"})
            response.status_code=486 #Client error
            return response
        else:
            response=jsonify({"message":"Sign in successful"})
            response.status_code=201
            return response
    except:
        response=jsonify({"message":"Something went wrong"})
        response.status_code=501
        return response

    # route to fetch the conference rooms
@app.route("/getconference_room",methods=["GET"])
def conferenceroom():
    con = pymysql.connect(host="keithwarui50.mysql.pythonanywhere-services.com", user="keithwarui50",
                      password="VANAlito1997", database="keithwarui50$default")
#     sql to be executed
    sql='select * from conference_room'
#     create a cursor to execute the sql
    cursor=con.cursor()
#     execute the sql
    cursor.execute(sql)
#     some validation checks to check if there's any records to fetch
    if cursor.rowcount == 0:
        response=jsonify({"message":"No products available"})
        response.status_code == 407
        return response
    else:
        rooms=cursor.fetchall()
        response=jsonify(rooms)_#fetch the records in json format
        response.status_code==205
        return response

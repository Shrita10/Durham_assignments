# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:01:03 2021

@author: Shrita
"""

from flask import Flask, jsonify, json
import mysql.connector
from mysql.connector import MySQLConnection

app = Flask(__name__)


    
def create_conn():
    conn = MySQLConnection(host = "127.0.0.1" , user = "root" ,password = "1243" , database = "shrita", auth_plugin='mysql_native_password')
    return conn



@app.route("/readStudent")
def readStudent():
    query = "SELECT * FROM shrita.asgn3 where first_name = 'gbemisola';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    resp = jsonify(row)
    return(resp)

@app.route("/readAll")
def readAll():
    query = "SELECT * FROM shrita.asgn3"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    resp = jsonify(row)
    return(resp)



@app.route('/createStudent')
def createStudent():
    student_id = "5"
    first_name = "Kylie"
    last_name = "pitt"
    dob = "2000-06-16"
    amount_due = "50000"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO shrita.asgn3(student_id, first_name, last_name, dob, amount_due) VALUES (%s, %s, %s, %s, %s)", (student_id, first_name, last_name, dob, amount_due))
    conn.commit()
    return "record created"   




@app.route("/updateRecord")
def updateRecord():
    query = "UPDATE shrita.asgn3 SET amount_due = 100 WHERE first_name = 'Gbemisola';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return "record updated"

@app.route("/deleteRecord")
def deleteRecord():
    query = "DELETE FROM shrita.asgn3 where student_id = '4';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return "Deleted record"




if __name__ == '__main__':
    app.run(debug=True)
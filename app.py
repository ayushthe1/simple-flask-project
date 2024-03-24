# import os
# from flask import Flask, jsonify, render_template, request
# import pymysql

# app = Flask(__name__)

# rds_host = None

# def get_db_connection():
#     global rds_host
#     if not rds_host:
#         raise ValueError("RDS endpoint environment variable not set")
#     connection = pymysql.connect(host=rds_host,  # Replace with your RDS endpoint
#                                  user='dbuser',      # Replace with your RDS username
#                                  password='dbpassword',  # Replace with your RDS password
#                                  db='devprojdb',   # Replace with your database name
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor)
#     return connection

# @app.route('/health')
# def health():
#     return "Up & Running"

# @app.route('/create_table')
# def create_table():
#     connection = get_db_connection()
#     cursor = connection.cursor() #  creates a cursor object associated with the database connection. The cursor is used to execute SQL queries.
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS example_table (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL
#         )
#     """
#     cursor.execute(create_table_query)
#     connection.commit()
#     connection.close()
#     return "Table created successfully"

# @app.route('/insert_record', methods=['POST'])
# def insert_record():
#     name = request.json['name']
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     insert_query = "INSERT INTO example_table (name) VALUES (%s)"
#     cursor.execute(insert_query, (name,))
#     connection.commit()
#     connection.close()
#     return "Record inserted successfully"

# @app.route('/data')
# def data():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM example_table')
#     result = cursor.fetchall()
#     connection.close()
#     return jsonify(result)

# # UI route
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')


import os
from flask import Flask, jsonify, render_template, request
import pymysql

app = Flask(__name__)

rds_host = None

def get_db_connection():
    global rds_host
    if not rds_host:
        raise ValueError("RDS host connection string not provided")
    connection = pymysql.connect(host=rds_host,
                                 user='dbuser',
                                 password='dbpassword',
                                 db='devprojdb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/health')
def health():
    return "Up & Running"

@app.route('/create_table')
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor() #  creates a cursor object associated with the database connection. The cursor is used to execute SQL queries.
    create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    return "Table created successfully"

@app.route('/insert_record', methods=['POST'])
def insert_record():
    name = request.json['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO example_table (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    connection.commit()
    connection.close()
    return "Record inserted successfully"

@app.route('/data')
def data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')
    result = cursor.fetchall()
    connection.close()
    return jsonify(result)

@app.route('/set_rds_host', methods=['POST'])
def set_rds_host():
    global rds_host
    rds_host = request.json['rdsHost']
    return f"RDS host connection string set successfully: {rds_host}"  # Let's return the received value for debugging

# UI route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

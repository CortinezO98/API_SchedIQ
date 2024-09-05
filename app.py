from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='jcortinez7.mysql.pythonanywhere-services.com',
            user='jcortinez7',
            password='Jolucoma1998-*@',  
            database='jcortinez7$default'  
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/get-data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM agendamiento')  
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

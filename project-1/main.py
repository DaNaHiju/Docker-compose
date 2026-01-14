from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

# Connect to the MySQL database
mysql_host = os.environ.get('MYSQL_HOST', 'mysql')
mysql_port = int(os.environ.get('MYSQL_PORT', 3306))
mysql_db = os.environ.get('MYSQL_DB', 'your_db_name')
mysql_user = os.environ.get('MYSQL_USER', 'your_db_user')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'your_db_password')

# Create a MySQL connection
mysql_conn = mysql.connector.connect(
    host=mysql_host,
    port=mysql_port,
    database=mysql_db,
    user=mysql_user,
    password=mysql_password
)

# Create a cursor to execute SQL queries
mysql_cursor = mysql_conn.cursor()

@app.route('/')
def index():
    # Increment the page counter in MySQL
    update_counter_query = f"""
        INSERT INTO page_counter (count) VALUES (1)
        ON DUPLICATE KEY UPDATE count = count + 1;
    """

    mysql_cursor.execute(update_counter_query)

    # Commit the changes
    mysql_conn.commit()

    return render_template('index.html', page_count=mysql_cursor.lastrowid)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

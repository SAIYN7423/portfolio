import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('contact_details sqllite.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('portfolio.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO contected_details (name, email, phone, message) VALUES (?, ?, ?, ?)',
            (name, email, phone, message)
        )
        conn.commit()
        conn.close()

        return 'Thanks for contacting me!'

    return render_template('form.html')

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('data.db')  # clean filename
    conn.row_factory = sqlite3.Row
    return conn

# Home route (main portfolio page)
@app.route('/')
def home():
    return render_template('portfolio.html')

# Contact form route
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

if __name__ == '__main__':
    app.run(debug=True)

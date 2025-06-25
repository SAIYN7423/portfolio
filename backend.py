from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# ✅ PostgreSQL connection
def get_db_connection():
    conn = psycopg2.connect(
        host='dpg-d1doe2p5pdvs73ap6vpg-a.oregon-postgres.render.com',
        database='portfolio_db_zdkt',
        user='portfolio_db_zdkt_user',
        password='bae8AzvstLyDZWvKlgHXAhmgreQ9uDNM',
        port='5432'
    )
    return conn

# ✅ Create table if it doesn't exist
def init_postgres():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contected_details (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            message TEXT
        );
    ''')
    conn.commit()
    conn.close()

# Initialize DB table
init_postgres()

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
            'INSERT INTO contected_details (name, email, phone, message) VALUES (%s, %s, %s, %s)',
            (name, email, phone, message)
        )
        conn.commit()
        conn.close()

        return 'Thanks for contacting me!'
    
    return render_template('form.html')

# ✅ Required for Render to detect your Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

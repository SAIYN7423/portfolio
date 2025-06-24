from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7423",  # change if needed
    database="contected_details"
)
cursor = db.cursor()

# Home (Portfolio)
@app.route("/")
def home():
    return render_template("portfolio.html")  # portfolio page

# Contact Form Page
@app.route("/form")
def form():
    return render_template("form.html")  # form page

# Form Submission Handler
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    message = request.form["message"]

    query = "INSERT INTO details (name, phone, email, message) VALUES (%s, %s, %s, %s)"
    values = (name, phone, email, message)
    cursor.execute(query, values)
    db.commit()

    return "<h2 style='text-align:center; color:green;'>Form submitted successfully!</h2>"

if __name__ == "__main__":
    app.run(debug=True)

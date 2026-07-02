from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY13424_SECRET23342_KEY_In_this_app_till_now_for_no000one-descovery'
db = sqlite3.connect('database_development.db', check_same_thread=False)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)
    app.run()
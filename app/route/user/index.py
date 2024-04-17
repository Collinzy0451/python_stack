from app import app 
from flask import render_template


@app.route("/user")
def user_home_page():



    return render_template("user/home.html")
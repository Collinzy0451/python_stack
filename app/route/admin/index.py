from app import app 
from flask import render_template


@app.route("/admin")
def admin_page():

    return render_template("admin/home.html")


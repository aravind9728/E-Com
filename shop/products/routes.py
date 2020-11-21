from flask import redirect,render_template,flash,url_for,request
form shop import db, app

app.routes('/addbrand', methods=['GET','POST'])
def addbrand():
    return render_template('products/addbrand.html')
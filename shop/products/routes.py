from flask import redirect,render_template,flash,url_for,request
from shop import db, app
from .modules import Brand, Category

@app.route('/addbrand', methods=['GET','POST'])
def addbrand():

    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'the brand {getbrand} was added to database', 'success')
        db.session.commit()
        return redirect(url_for("addbrand"))


    
    return render_template('products/addbrand.html',brands='brands')



@app.route('/addcat', methods=['GET','POST'])
def addcat():

    if request.method == "POST":
        getbrand = request.form.get('category')
        cat = Brand(name=getbrand)
        db.session.add(cat)
        flash(f'the category {getbrand} was added to database', 'success')
        db.session.commit()
        return redirect(url_for("addcat"))


    
    return render_template('products/addbrand.html')
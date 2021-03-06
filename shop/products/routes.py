from flask import redirect,render_template,flash,url_for,request,session
from shop import db, app, photos
from .modules import Brand, Category, Addproduct
from .forms import AddProducts
import secrets

@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if 'email' not in session:
        flash(f"Warning please login to access this page",'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'the brand {getbrand} was added to database', 'success')
        db.session.commit()
        return redirect(url_for("addbrand"))


    
    return render_template('products/addbrand.html',brands='brands')

@app.route('/updatebrand/<int:id>', methods= ['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f"Warning please login to access this page",'danger')
        updatebrand = Brand.query.get_or_404(id)
        brand = request.form.get('brand')
        if request.method=='POST':
            updatebrand.name = brand
            flash(f'Your brand has been updated', 'success')
            db.session.commit()
            return redirect(url_for('brands'))
        return render_template('products/updatebrand.html', title ='Update brand page',updatebrand=updatebrand)

@app.route('/addcategory', methods=['GET','POST'])
def addcategory():
    if 'email' not in session:
        flash(f"Warning please login to access this page",'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'the category {getcategory} was added to database', 'success')
        db.session.commit()
        return redirect(url_for("addcategory"))


    
    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    if 'email' not in session:
        flash(f"Warning please login to access this page",'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProducts(request.form)
    if request.method == 'POST':
        name  = form.name.data
        price = form.price.data 
        discount = form.discount.data  
        stock = form.stock.data 
        colors = form.colors.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")
        addpro = Addproduct(name=name, price=price,discount=discount,stock=stock,colors=colors,desc=desc,brand_id=brand,category_id=category,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addpro)
        flash(f"The product{name} has been added to the database", 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form = form, title="Add Product page", brands=brands, categories=categories)
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Car, CarImage
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autohunt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    status_filter = request.args.get('status')
    make_filter = request.args.get('make')
    sort_by = request.args.get('sort', 'created_at')
    sort_order = request.args.get('order', 'desc')

    query = Car.query

    if status_filter:
        query = query.filter_by(status=status_filter)
    if make_filter:
        query = query.filter_by(make=make_filter)

    if sort_order == 'asc':
        query = query.order_by(getattr(Car, sort_by).asc())
    else:
        query = query.order_by(getattr(Car, sort_by).desc())

    cars = query.all()
    makes = db.session.query(Car.make).distinct().all()
    
    return render_template('index.html', 
                         cars=cars, 
                         makes=makes,
                         status_filter=status_filter,
                         make_filter=make_filter,
                         sort_by=sort_by,
                         sort_order=sort_order)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        try:
            car = Car(
                year=request.form['year'],
                make=request.form['make'],
                model=request.form['model'],
                listing_link=request.form['listing_link'],
                status=request.form['status'],
                price=float(request.form['price']) if request.form['price'] else None,
                mileage=int(request.form['mileage']) if request.form['mileage'] else None,
                engine_cylinders=int(request.form['engine_cylinders']) if request.form['engine_cylinders'] else None,
                engine_displacement=float(request.form['engine_displacement']) if request.form['engine_displacement'] else None,
                drivetrain=request.form['drivetrain'],
                carfax_link=request.form['carfax_link']
            )
            db.session.add(car)
            db.session.commit()

            # Handle image uploads
            if 'images' in request.files:
                for file in request.files.getlist('images'):
                    if file.filename != '':
                        filename = secure_filename(file.filename)
                        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file.save(filepath)
                        
                        car_image = CarImage(
                            car_id=car.id,
                            filename=filename,
                            is_primary=False
                        )
                        db.session.add(car_image)
                
                db.session.commit()

            flash('Car added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding car: {str(e)}', 'danger')
    
    return render_template('add_car.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    car = Car.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            car.year = request.form['year']
            car.make = request.form['make']
            car.model = request.form['model']
            car.listing_link = request.form['listing_link']
            car.status = request.form['status']
            car.price = float(request.form['price']) if request.form['price'] else None
            car.mileage = int(request.form['mileage']) if request.form['mileage'] else None
            car.engine_cylinders = int(request.form['engine_cylinders']) if request.form['engine_cylinders'] else None
            car.engine_displacement = float(request.form['engine_displacement']) if request.form['engine_displacement'] else None
            car.drivetrain = request.form['drivetrain']
            car.carfax_link = request.form['carfax_link']
            car.updated_at = datetime.utcnow()
            
            db.session.commit()
            flash('Car updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating car: {str(e)}', 'danger')
    
    return render_template('edit_car.html', car=car)

@app.route('/view/<int:id>')
def view_car(id):
    car = Car.query.get_or_404(id)
    return render_template('view_car.html', car=car)

@app.route('/delete/<int:id>')
def delete_car(id):
    car = Car.query.get_or_404(id)
    try:
        # Delete associated images
        for image in car.images:
            try:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            except:
                pass
            db.session.delete(image)
        
        db.session.delete(car)
        db.session.commit()
        flash('Car deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting car: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
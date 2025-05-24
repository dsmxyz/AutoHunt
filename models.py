from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    listing_link = db.Column(db.String(500))
    status = db.Column(db.String(20), nullable=False, default='available')
    price = db.Column(db.Float)
    mileage = db.Column(db.Integer)
    engine_cylinders = db.Column(db.Integer)
    engine_displacement = db.Column(db.Float)
    drivetrain = db.Column(db.String(50))
    carfax_link = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    images = db.relationship('CarImage', backref='car', lazy=True)

    def __repr__(self):
        return f'<Car {self.year} {self.make} {self.model}>'

class CarImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    is_primary = db.Column(db.Boolean, default=False)
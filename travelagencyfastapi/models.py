from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Float,Date
class Customers(Base):
    __tablename__="customers"
    customer_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    email=Column(String)
    phone=Column(Integer)
    address=Column(String)
class Package(Base):
    __tablename__="package"
    package_id=Column(String,primary_key=True)
    package_name=Column(String)
    destination=Column(String)
    duration=Column(String)
    price=Column(Float)
    startdate=Column(Date)
    enddate=Column(Date)
class Hotel(Base):
    __tablename__="hotel"
    hotel_id=Column(String,primary_key=True)
    package_id=Column(String,ForeignKey('package.package_id'))
    hotel_name=Column(String)
    location=Column(String)
    rating=Column(Float)
class Bookings(Base):
    __tablename__="bookings"
    booking_id=Column(String,primary_key=True)
    package_id=Column(String,ForeignKey('package.package_id'))
    customer_id=Column(Integer,ForeignKey('customers.customer_id'))
    booking_date=Column(Date)
    status=Column(String)
class Staff(Base):
    __tablename__="staff"
    staff_id=Column(String,primary_key=True)
    name=Column(String)
    role=Column(String)
    email=Column(String)
    phone=Column(Integer)


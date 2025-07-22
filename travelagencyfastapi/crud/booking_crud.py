from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Customers,Bookings,Package
from schemas import BookingRead,MostBooked,Payment_confirmed_Customers,Payment_pending_Customers,PackageWithBooking
from typing import List
async def read_all_bookings(db:AsyncSession)->List[Bookings]:
    result=await db.execute(select(Bookings))
    db_booking=result.scalars().all()
    return db_booking
async def read_booking_by_id(booking_id:str,db:AsyncSession)->BookingRead:
    result=await db.execute(select(Bookings).filter(Bookings.booking_id==booking_id))
    db_booking=result.scalars().first()
    return db_booking
async def create_new_booking(booking:BookingRead,db:AsyncSession)->BookingRead:
    db_new_booking=Bookings(booking_id=booking.booking_id,package_id=booking.package_id,customer_id=booking.customer_id,booking_date=booking.booking_date,status=booking.status)
    db.add(db_new_booking)
    await db.commit()
    await db.refresh(db_new_booking)
    return db_new_booking

async def read_payment_pending_customer_details(db:AsyncSession)->List[Payment_pending_Customers]:
    stmt=(
        select(Customers.customer_id,Customers.name, Customers.phone,Customers.email,Customers.address,Bookings.status). 
        join (Bookings, Customers.customer_id==Bookings.customer_id).
        where(Bookings.status=='payment pending'))
    result= await db.execute(stmt)
    db_customers=result.all()
    return db_customers
async def read_confirmed_customer_details(db:AsyncSession)->List[Payment_confirmed_Customers]:
    stmt=(
        select(Customers.customer_id,Customers.name, Customers.phone,Customers.email,Customers.address,Bookings.status). 
        join (Bookings, Customers.customer_id==Bookings.customer_id).
        where(Bookings.status=='confirmed'))
    result= await db.execute(stmt)
    db_customers=result.all()
    return db_customers
async  def read_package_with_booking_id(booking_id:str,db:AsyncSession)->PackageWithBooking:
    stmt=(select(Bookings.booking_id,Package.package_id,Package.package_name,Package.destination,Package.duration,Package.startdate,Package.enddate,Package.price).
          join(Package,Package.package_id==Bookings.package_id).
          where(Bookings.booking_id==booking_id))
    result= await db.execute(stmt)
    db_packages=result.first()
    return db_packages
async def read_most_booked_package(db:AsyncSession)->List[MostBooked]:
    stmt=(select(Bookings.package_id,Package.package_name,Package.destination,Package.price,(func.count(Bookings.package_id)).label("counts")).
          join(Bookings,Bookings.package_id==Package.package_id).
          group_by(Bookings.package_id,Package.package_name,Package.destination,Package.price).
          order_by(Bookings.package_id)
        )
    result=await db.execute(stmt)
    db_package=result.all()
    return db_package

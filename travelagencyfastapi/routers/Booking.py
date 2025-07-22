from fastapi import APIRouter, Depends, HTTPException,status
from schemas import BookingBy_Id, BookingRead, MostBooked, PackageWithBooking, Payment_pending_Customers,Payment_confirmed_Customers
from sqlalchemy.ext.asyncio import AsyncSession
from database import  get_db
from typing import List
from crud import booking_crud
router=APIRouter()
@router.get("/booking",response_model=List[BookingRead])
async def show_all_bookings(db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_all_bookings(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no booking details")
@router.get("/booking/{booking_id}",response_model=BookingRead)
async def show_booking_by_id(booking_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_booking_by_id(booking_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no booking details")
@router.post("/booking",response_model=BookingBy_Id)
async def add_new_booking(booking:BookingRead,db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.create_new_booking(booking,db)
    return db_result
@router.get("/bookings/payment_pending",response_model=List[Payment_pending_Customers])
async def show_payment_pending_customer_details(db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_payment_pending_customer_details(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such details")
@router.get("/bookings/payment_confirmed",response_model=List[Payment_confirmed_Customers])
async def show_confirmed_customer_details(db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_confirmed_customer_details(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such details")
@router.get("/bookings/{booking_id}/package",response_model=PackageWithBooking)
async  def show_package_with_booking_id(booking_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_package_with_booking_id(booking_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such details")
@router.get("/bookings/mostbooked",response_model=List[MostBooked])
async def most_booked_package(db:AsyncSession=Depends(get_db)):
    db_result=await booking_crud.read_most_booked_package(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such details")
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Hotel
from schemas import Hotel_By_Id,HotelCreate,HotelRead
from typing import List

async def read_all_hotels(db:AsyncSession)->List[HotelRead]:
    result=await db.execute(select(Hotel))
    db_hotel=result.scalars().all()
    return db_hotel
async def read_hotel_by_id(hotel_id:str,db:AsyncSession)->HotelRead:
    result=await db.execute(select(Hotel).filter(Hotel.hotel_id==hotel_id))
    db_hotel=result.scalars().first()
    return db_hotel
async def create_new_hotel(hotel:HotelCreate,db:AsyncSession)->Hotel_By_Id:
    db_new_hotel=Hotel(hotel_id=hotel.hotel_id,package_id=hotel.package_id,hotel_name=hotel.hotel_name,location=hotel.location,rating=hotel.rating)
    db.add(db_new_hotel)
    await db.commit()
    await db.refresh(db_new_hotel)
    return db_new_hotel
async def updating_hotel(hotel_id:str,hotel:HotelRead,db:AsyncSession)->Hotel_By_Id:
    result=await db.execute(select(Hotel).filter(Hotel.hotel_id==hotel_id))
    db_hotel=result.scalars().first()
    if db_hotel:
        db_hotel.hotel_id=hotel.hotel_id
        db_hotel.package_id=hotel.package_id
        db_hotel.hotel_name=hotel.hotel_name
        db_hotel.location=hotel.location
        db_hotel.rating=hotel.rating
        await db.commit()
        await db.refresh(db_hotel)
        return db_hotel
async def deleting_hotel(hotel_id:str,db:AsyncSession)->Hotel_By_Id:
    result=await db.execute(select(Hotel).filter(Hotel.hotel_id==hotel_id))
    db_hotel=result.scalars().first()
    if db_hotel:
        await db.delete(db_hotel)
        await db.commit()
        return db_hotel
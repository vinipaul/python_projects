from fastapi import APIRouter, Depends, HTTPException,status
from schemas import  Hotel_By_Id, HotelRead,HotelCreate
from sqlalchemy.ext.asyncio import AsyncSession
from database import  get_db
from typing import List
from crud import hotel_crud
router=APIRouter()
@router.get("/hotels",response_model=List[HotelRead])
async def show_all_hotels(db:AsyncSession=Depends(get_db)):
    db_result=await hotel_crud.read_all_hotels(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no hotel details")
@router.get("/hotels/{hotel_id}",response_model=HotelRead)
async def show_hotel_by_id(hotel_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await hotel_crud.read_hotel_by_id(hotel_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="hotel is unavailable")
@router.post("/hotels",response_model=Hotel_By_Id)
async def add_new_hotel(hotel:HotelCreate,db:AsyncSession=Depends(get_db)):
    db_result=await hotel_crud.create_new_hotel(hotel,db)
    return db_result
@router.put("/hotels/{hotel_id}",response_model=Hotel_By_Id)
async def update_hotel(hotel_id:str,hotel:HotelRead,db:AsyncSession=Depends(get_db)):
    db_result=await hotel_crud.updating_hotel(hotel_id,hotel,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="hotel is unavailable")
@router.delete("/hotels/{hotel_id}",response_model=Hotel_By_Id)
async def delete_hotel(hotel_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await hotel_crud.deleting_hotel(hotel_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="hotel is unavailable")
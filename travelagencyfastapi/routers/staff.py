from fastapi import APIRouter, Depends, HTTPException,status
from schemas import  Staff_By_Id, StaffCreate, StaffRead
from sqlalchemy.ext.asyncio import AsyncSession
from database import  get_db
from typing import List
from crud import staff_crud
router=APIRouter()
@router.get("/staff",response_model=List[StaffRead])
async def show_all_staff(db:AsyncSession=Depends(get_db)):
    db_result=await staff_crud.read_all_staff(db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no staff details")
@router.get("/staff/{staff_id}",response_model=StaffRead)
async def show_staff_by_id(staff_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await staff_crud.read_staff_by_id(staff_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="staff is unavailable")

@router.post("/staff",response_model=Staff_By_Id)
async def add_new_staff(staff:StaffCreate,db:AsyncSession=Depends(get_db)):
    db_result=await staff_crud.create_new_staff(staff,db)
    return db_result

@router.put("/staff/{staff_id}",response_model=Staff_By_Id)
async def updating_staff(staff_id:str,staff:StaffCreate,db:AsyncSession=Depends(get_db)):
    db_result=await staff_crud.update_staff(staff_id,staff,db)
    if db_result:
         return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="staff is unavailable")
@router.delete("/staff/{staff_id}",response_model=Staff_By_Id)
async def deleting_staff(staff_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await staff_crud.delete_staff(staff_id,db)
    if db_result:
         return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="staff is unavailable")


    
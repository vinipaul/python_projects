from fastapi import APIRouter, Depends, HTTPException,status
from schemas import  PackageRead, PackageReadId, PackageUpdate, packageCreate
from sqlalchemy.ext.asyncio import AsyncSession
from database import  get_db
from typing import List
from crud import package_crud
router=APIRouter()
@router.get("/package",response_model=List[PackageRead])
async def show_all_packages(db:AsyncSession=Depends(get_db)):
    db_result=await package_crud.read_all_packages(db)
    if db_result:
        return db_result
    else:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="packages unavailable")
@router.post("/packages",response_model=PackageReadId)
async def add_new_package(package:packageCreate,db:AsyncSession=Depends(get_db)):
    db_result=await package_crud.create_new_package(package,db)
    return db_result
@router.get("/packages/{package_id}",response_model=PackageRead)
async def show_package_by_id(package_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await package_crud.read_package_by_id(package_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=404,detail="package is unavailable")
@router.put("/packages/{package_id}",response_model=PackageReadId)
async def updating_package(package_id:str,package:PackageUpdate,db:AsyncSession=Depends(get_db)):
    db_result=await package_crud.update_package(package_id,package,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="package is unavailable")
@router.delete("/packages/{package_id}",response_model=PackageReadId)
async def package_deleting(package_id:str,db:AsyncSession=Depends(get_db)):
    db_result=await package_crud.delete_package(package_id,db)
    if db_result:
        return db_result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="package is unavailable")
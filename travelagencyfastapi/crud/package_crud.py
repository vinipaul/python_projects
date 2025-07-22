from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Package
from schemas import packageCreate,PackageRead,PackageReadId,PackageUpdate
from typing import List
async def read_all_packages(db:AsyncSession)->List[Package]:
    result=await db.execute(select(Package))
    db_packages=result.scalars().all()
    return db_packages
async def create_new_package(package:packageCreate,db:AsyncSession)->PackageReadId:
    db_new_package=Package(package_id=package.package_id,package_name=package.package_name,destination=package.destination,duration=package.duration,price=package.price,startdate=package.startdate,enddate=package.enddate)
    db.add(db_new_package)
    await db.commit()
    await db.refresh(db_new_package)
    return db_new_package
async def read_package_by_id(package_id:str,db:AsyncSession)->PackageRead:
    result=await db.execute(select(Package).filter(Package.package_id==package_id))
    db_package=result.scalars().first()
    if db_package:
        return db_package
    else:
        return None
async def update_package(package_id:str,package:PackageUpdate,db:AsyncSession)->PackageReadId:
    result=await db.execute(select(Package).filter(Package.package_id==package_id))
    db_package=result.scalars().first()
    if db_package:
        db_package.package_name=package.package_name
        db_package.destination=package.destination
        db_package.duration=package.duration
        db_package.price=package.price
        db_package.startdate=package.startdate
        db_package.enddate=package.enddate
        await db.commit()
        await db.refresh(db_package)
    return db_package
async def delete_package(package_id:str,db:AsyncSession)->PackageReadId:
    result=await db.execute(select(Package).filter(Package.package_id==package_id))
    db_result=result.scalars().first()
    if db_result:
        await db.delete(db_result)
        await db.commit()
    return db_result
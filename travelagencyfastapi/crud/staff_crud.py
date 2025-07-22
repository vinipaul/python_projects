from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Staff
from schemas import Staff_By_Id,StaffCreate,StaffRead
from typing import List
async def read_all_staff(db:AsyncSession)->List[Staff]:
    result=await db.execute(select(Staff))
    db_staff=result.scalars().all()
    return db_staff
async def read_staff_by_id(staff_id:str,db:AsyncSession)->StaffRead:
    result=await db.execute(select(Staff).filter(Staff.staff_id==staff_id))
    db_staff=result.scalars().first()
    if db_staff:
        return db_staff
async def create_new_staff(staff:StaffCreate,db:AsyncSession)->Staff_By_Id:
    db_new_staff=Staff(staff_id=staff.staff_id,name=staff.name,role=staff.role,email=staff.email,phone=staff.phone)
    db.add(db_new_staff)
    await db.commit()
    await db.refresh(db_new_staff)
    return db_new_staff
async def update_staff(staff_id:str,staff:StaffCreate,db:AsyncSession)->Staff_By_Id:
    result=await db.execute(select(Staff).filter(Staff.staff_id==staff_id))
    db_staff=result.scalars().first()
    if db_staff:
        db_staff.staff_id=staff.staff_id
        db_staff.name=staff.name
        db_staff.role=staff.role
        db_staff.email=staff.email
        db_staff.phone=staff.phone
        await db.commit()
        await db.refresh(db_staff)
    return db_staff
async def delete_staff(staff_id:str,db:AsyncSession)->Staff_By_Id:
    result=await db.execute(select(Staff).filter(Staff.staff_id==staff_id))
    db_staff=result.scalars().first()
    if db_staff:
        await db.delete(db_staff)
        await db.commit()
    return db_staff

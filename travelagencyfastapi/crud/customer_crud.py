from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import CustomerById, CustomerCreate, CustomerRead, CustomerUpdate,CustomerResponse
from typing import List
from models import Customers

async def get_all_customers(db: AsyncSession)->List[CustomerRead]:
    result = await db.execute(select(Customers))
    customers= result.scalars().all()
    return customers
async def add_customer(customer: CustomerCreate, db: AsyncSession)->CustomerResponse:
    new_customer = Customers(name=customer.name, email=customer.email,phone=customer.phone,address=customer.address)
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer.customer_id

async def get_customer_by_id(customer_id:int,db: AsyncSession )->CustomerRead:
    result = await db.execute(select(Customers).filter(Customers.customer_id==customer_id))
    customers= result.scalars().first()
    return customers
async def updating_customer(customer_id:int,customer:CustomerUpdate,db:AsyncSession)->CustomerResponse:
    result=await db.execute(select(Customers).filter(Customers.customer_id==customer_id))
    db_customers=result.scalars().first()
    if db_customers:
        db_customers.name=customer.name
        db_customers.email=customer.email
        db_customers.address=customer.address
        db_customers.phone=customer.phone
        await db.commit()
        await db.refresh(db_customers)
        return db_customers.customer_id
async def deleting_customer(customer_id:int,db:AsyncSession)->CustomerRead:
    result=await db.execute(select(Customers).filter(Customers.customer_id==customer_id))
    db_result=result.scalars().first()
    if db_result:
        await db.delete(db_result)
        await db.commit()
        return db_result
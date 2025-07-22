from fastapi import APIRouter, Depends, HTTPException,status
from schemas import CustomerById, CustomerCreate, CustomerRead, CustomerUpdate,CustomerResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database import  get_db
from typing import List
from crud import customer_crud
router=APIRouter()

@router.get("/customers",response_model=List[CustomerRead])
async def show_all_customers(db: AsyncSession = Depends(get_db)):
    customer_db=await customer_crud.get_all_customers(db)
    if customer_db:
        return customer_db
    else:
        raise HTTPException(status_code=404,detail="customer not found")
@router.post("/customers",response_model=CustomerResponse)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    new_customer_db=await customer_crud.add_customer(customer,db)
    return {"message":"added successfully","content":CustomerById(customer_id=new_customer_db)}
@router.get("/customers/{customer_id}",response_model=CustomerRead)
async def show_customer_by_id(customer_id:int,db: AsyncSession = Depends(get_db)):
    customers_db=await customer_crud.get_customer_by_id(customer_id,db)
    if customers_db:
        return customers_db
    else:
         raise HTTPException(status_code=404,detail= "customer not found")
@router.put("/customers/{customer_id}",response_model=CustomerResponse)
async def update_customer(customer_id:int,customer:CustomerUpdate,db:AsyncSession=Depends(get_db)):
    customer_db=await customer_crud.updating_customer(customer_id,customer,db)
    if customer_db:
        return {"message":"updated successfully","content":CustomerById(customer_id=customer_db)}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer not found")
@router.delete("/customers/{customer_id}",response_model=CustomerRead)
async def customer_delete(customer_id:int,db:AsyncSession=Depends(get_db)):
    db_result=await customer_crud.deleting_customer(customer_id,db)
    if db_result:
        return db_result
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="customer not found")
    
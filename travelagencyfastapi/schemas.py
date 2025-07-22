import datetime
from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: int
    address: str
class CustomerById(BaseModel):
   customer_id: int 
   class Config: 
      orm_mode = True
class CustomerResponse(BaseModel):
   message:str
   content:CustomerById
   class Config: 
      orm_mode = True
class CustomerRead(BaseModel):
    customer_id: int  
    name: str
    email: str
    phone: int
    address: str
    class Config: 
      orm_mode = True
class CustomerUpdate(BaseModel):
    name: str
    email:str
    phone: int
    address: str



class packageCreate(BaseModel):
   package_id:str
   package_name:str
   destination:str
   duration:str
   price:float
   startdate:datetime.date
   enddate:datetime.date
class PackageRead(BaseModel):
   package_id:str
   package_name:str
   destination:str
   duration:str
   price:float
   startdate:datetime.date
   enddate:datetime.date
   class Config:
       orm_mode=True
class PackageUpdate(BaseModel):
   package_name:str
   destination:str
   duration:str
   price:float
   startdate:datetime.date
   enddate:datetime.date
class PackageReadId(BaseModel):
    package_id:str
    class Config:
       orm_mode=True



class StaffRead(BaseModel):
   staff_id:str
   name:str
   role:str
   email:str
   phone:int
   class config:
      orm_mode=True
class Staff_By_Id(BaseModel):
   staff_id:str
   class config:
      orm_mode=True
class StaffCreate(BaseModel):
   staff_id:str
   name:str
   role:str
   email:str
   phone:int

class HotelCreate(BaseModel):
   hotel_id:str
   package_id:str
   hotel_name:str
   location:str
   rating:float  
class HotelRead(BaseModel):
   hotel_id:str
   package_id:str
   hotel_name:str
   location:str
   rating:float  
   class config:
      orm_mode=True  
class Hotel_By_Id(BaseModel):
   hotel_id:str
   class config:
      orm_mode=True 


class BookingRead(BaseModel):
    booking_id:str
    package_id:str
    customer_id:int
    booking_date:datetime.date
    status:str
    class config:
      orm_mode=True  
class BookingBy_Id(BaseModel):
    booking_id:str
    class config:
      orm_mode=True  
class Payment_pending_Customers(BaseModel):
   customer_id: int  
   name: str
   email: str
   phone: int
   address: str
   status:str
   class config:
      orm_mode=True  
class Payment_confirmed_Customers(BaseModel):
   customer_id: int  
   name: str
   email: str
   phone: int
   address: str
   status:str
   class config:
      orm_mode=True  
class PackageWithBooking(BaseModel):
   booking_id:str
   package_id:str
   package_name:str
   destination:str
   duration:str
   price:float
   startdate:datetime.date
   enddate:datetime.date
   class config:
      orm_mode=True  
class MostBooked(BaseModel):
   package_id:str
   package_name:str
   destination:str
   price:float
   counts:int
   class config:
      orm_mode=True  
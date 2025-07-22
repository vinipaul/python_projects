
from fastapi import FastAPI
from models import Base
from database import engine
from routers.customers import router as customers_router
from routers.Booking import router as booking_router
from routers.package import router as package_router
from routers.staff import router as staff_router
from routers.hotels import router as hotel_router
app=FastAPI()
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
app.include_router(customers_router,tags=["Customers"] )
app.include_router(booking_router,tags=["Booking"] )
app.include_router(package_router,tags=["Packages"] )
app.include_router(staff_router,tags=["Staff"] )
app.include_router(hotel_router,tags=["Hotel"] )

from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
DATABASE_URL="postgresql+asyncpg://postgres:postgresvini@localhost:5432/fast_travel_db"
engine=create_async_engine(DATABASE_URL,echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autoflush=False,autocommit=False)
Base=declarative_base()
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings



class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.POSTGRES_DB_URL)


Session = async_sessionmaker(engine)

async def get_session():
    async with Session() as connect:
        yield connect
    




















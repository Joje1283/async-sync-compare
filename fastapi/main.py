from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from database import Base

from database import get_async_session, get_session

app = FastAPI()


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)


@app.get("/async-items/")
async def read_items(session: AsyncSession = Depends(get_async_session)):
    query = select(Item)
    result = await session.execute(query)
    result = result.scalars().all()
    return result


@app.get("/items/")
def read_items(session: Session = Depends(get_session)):
    query = select(Item)
    result = session.execute(query)
    result = result.scalars().all()
    return result


@app.get("/blocking-items/")
async def read_items(session: Session = Depends(get_session)):
    query = select(Item)
    result = session.execute(query)
    result = result.scalars().all()
    return result

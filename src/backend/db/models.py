from typing import Optional
from sqlalchemy import DateTime
from sqlmodel import SQLModel, Field, Column
import datetime


#class Hero(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    name: str
#    secret_name: str
#    age: Optional[int] = None
#    birth_date: Optional[datetime.datetime] = Field(sa_column=Column(DateTime(timezone=True), nullable=True))

class Plant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
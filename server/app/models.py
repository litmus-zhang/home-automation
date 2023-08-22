from enum import Enum
from typing import Optional
from pydantic import BaseModel,EmailStr
import sqlalchemy


class Role(str, Enum):
    Admin = 'admin'
    User = 'user'


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    role: Optional[Role] = Role.User

    class ConfigDict:
        from_attributes = True


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    role: Optional[Role] = Role.User
    pass

class UserPublic(UserBase):
    pass


class UserDB(UserBase):
    id: int
    pass
    

class DeviceBase(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: Optional[int] = None

    class ConfigDict:
        from_attributes = True


class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(DeviceBase):
    pin: Optional[str] = None
    pass

class DevicePublic(DeviceBase):
    pass

class DeviceDB(DeviceBase):
    id: int
    pass


metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String),
    sqlalchemy.Column("lastname", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("role", sqlalchemy.String),
)

devices = sqlalchemy.Table(
    "devices",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("owner_id", sqlalchemy.Integer),
    sqlalchemy.Column("pin", sqlalchemy.String),
)
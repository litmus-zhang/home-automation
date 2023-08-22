from fastapi import Body, Depends, FastAPI, status,HTTPException
from app.models import UserCreate, users, devices, metadata, UserUpdate, DeviceCreate, DeviceUpdate
from databases import Database
from app.config import get_database, database, sqlalchemy_engine

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/api/healthchecker")
async def root():
    return {"message": "System is OK"}


@app.post("/api/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, database : Database = Depends(get_database) ):
    insertQuery = users.insert().values(user.model_dump())
    # check if email exist in the database,
    # if yes, return error
    # if no, create user
    checkDuplicateQuery  = users.select().where(users.c.email == user.email)
    user = await database.fetch_one(checkDuplicateQuery)
    if user:
        raise HTTPException(status_code=400, detail="User already exist")
    else: 
        await database.execute(insertQuery)
        return {"message": "User created successfully"}


@app.get("/api/users", status_code=status.HTTP_200_OK)
async def get_all_users(database : Database = Depends(get_database)):
    query = users.select()
    return await database.fetch_all(query)

@app.get("/api/users/{id}")
async def get_user(id: int):
    query = database.select([users]).where(users.c.id == id)
    user = await database.fetch_one(query)
    return {"message": "User retrieved successfully", "data": user}


@app.put("/api/users/{id}")
async def update_user(id: int, updated_user: UserUpdate):
    user = await get_user(id)
    if user['data'] is None:
        raise HTTPException(status_code=404, detail="User not found")
    updateQuery = users.update().where(users.c.id == id).values(updated_user.model_dump())
    await database.execute(updateQuery)
    return {"message": "User updated successfully"}


@app.delete("/api/users/{id}")
async def delete_user(id: int):
    user = await get_user(id)
    if user['data'] is None:
        raise HTTPException(status_code=404, detail="User not found")
    deleteQuery = users.delete().where(users.c.id == id)
    await database.execute(deleteQuery)
    return {"message": "User deleted successfully"}


@app.get("/api/devices/")
async def get_devices(database : Database = Depends(get_database)):
    query = devices.select()
    allDevices = await database.fetch_all(query)
    return {"message": "Devices retrieved successfully", "data": allDevices}
  

@app.get("/api/devices/{id}")
async def get_device(id: int):
    deviceQuery = database.select([devices]).where(devices.c.id == id)
    device = await database.fetch_one(deviceQuery)
    return {"message": "Device retrieved successfully", "data": device}


@app.post("/api/devices/", status_code=status.HTTP_201_CREATED)
async def create_device(device: DeviceCreate , database : Database = Depends(get_database) ):
    insertQuery = devices.insert().values(device.model_dump())
    await database.execute(insertQuery)
    return {"message": "Device created successfully"}


@app.put("/api/devices/{id}")
async def update_device(id: int, updated_device: DeviceUpdate):
    updateQuery = devices.update().where(devices.c.id == id).values(updated_device.model_dump())
    await database.execute(updateQuery)
    return {"message": "Device updated successfully"}


@app.delete("/api/devices/{id}")
async def delete_device(id: int, database : Database = Depends(get_database)):
    deleteQuery = devices.delete().where(devices.c.id == id)
    await database.execute(deleteQuery)
    return {"message": "Device deleted successfully"}


@app.get("/api/users/{user_id}/devices/")
async def get_user_devices(user_id: int, database : Database = Depends(get_database)):
    query = devices.select().where(devices.c.owner_id == user_id)
    deviceList = await database.fetch_all(query)
    return {"message": "User devices retrieved successfully", "data": deviceList}


@app.get("/api/users/{user_id}/devices/{device_id}")
async def get_user_device(user_id: int, device_id: int, database : Database = Depends(get_database)):
    query = devices.select().where(devices.c.owner_id == user_id and devices.c.id == device_id)
    device = await database.fetch_one(query)
    return {"message": "User device retrieved successfully", "data": device}


@app.post("/api/users/{user_id}/devices/")
async def assign_device_to_user(user_id: int, device_id: int, database : Database = Depends(get_database) ):
    updateQuery = devices.update().where(devices.c.id == device_id).values(owner_id=user_id)
    await database.execute(updateQuery)
    return {"message": "User device created successfully"}

@app.post("/api/users/{user_id}/devices/{device_id}")
async def create_device_pin( device_id: int, pin: str, database : Database = Depends(get_database) ):
    updateQuery = devices.update().where(devices.c.id == device_id).values(pin=pin)
    await database.execute(updateQuery)
    return {"message": "Device pin created successfully"}


@app.put("/api/users/{user_id}/devices/{device_id}")
async def update_device_pin(user_id: int, device_id: int, pin: str, database : Database = Depends(get_database) ):
    updateQuery = devices.update().where(devices.c.id == device_id).values(pin=pin)
    await database.execute(updateQuery)
    return {"message": "Device pin updated successfully"}


@app.post("/api/users/{user_id}/devices/{device_id}")
async def enter_device_pin(pin : str, database : Database = Depends(get_database)):
    # enter pin, check if pin is valid for the device id, if yes, proceed, else raise an error
    comparePinQuery = devices.select().where(devices.c.pin == pin)
    device = await database.fetch_one(comparePinQuery)
    if device:
        return {"message": "Device pin is valid"}
    else:
        return {"message": "Invalid Pin"}
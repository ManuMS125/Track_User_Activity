from fastapi import FastAPI, APIRouter, HTTPException
from typing import Optional
from configurations import collection_name
from Database.schemas import list_serial
from Database.schemas import individual_serial
from Database.models import User
from bson.objectid import ObjectId

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
     'http://localhost:3000',
 ]



app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )
router=APIRouter()

@router.get('/')
async def get_hello_world():
     return 'HEllo, WOrld'


@router.get('/get/user')
async def get_all_data():
    users=list_serial(collection_name.find())
    return users


@router.get('/get/user/{name}')
async def get_particular_data(name: str):
    try:
        
        existing_user = collection_name.find_one({'name' : name})
        if not existing_user:
            return HTTPException(status_code=404, detail=print('name not exists.'))
        
        user = individual_serial(collection_name.find_one({'name':name}))
        return user
    except Exception as e:
        return HTTPException(status_code=500, detail=print('some error occurred', e)) 

@router.get('/get/user/{user_id}/')
async def get_particular_data(user_id: str):
    try:
        id = ObjectId(user_id)
        existing_user = collection_name.find_one({'_id' : id})
        if not existing_user:
            return HTTPException(status_code=404, detail=print('user_id not exists.'))
        
        user = individual_serial(collection_name.find_one({'_id':id}))
        return user
    except Exception as e:
        return HTTPException(status_code=500, detail=print('some error occurred', e)) 
    
@router.post('/create/user')
async def create_data(user: User):
    try:
        resp=collection_name.insert_one(dict(user))
        return {"status_code":200, 'id':str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=print('some error occurred', e))
    
@router.put('/update/user/{user_id}', response_model=User)
async def update_data(user_id: str, updated_user: User):
    try:
        id = ObjectId(user_id)
        existing_user = collection_name.find_one({'_id': id})
        if not existing_user:
            return HTTPException(status_code=404, detail=print('that id does not exist'))
        resp=collection_name.update_one({'_id':id}, {'$set': dict(updated_user)})
        return {'status code': 200, 'message':'user updated successfully'}
    
    
    except Exception as e:
        return HTTPException(status_code=500, detail=print('some error occurred', e))
    
@router.delete('/delete/user/{name}')
async def delete_data(name: str):
    try:
        
        existing_user = collection_name.find_one({'name':name})
        if not existing_user:
            return HTTPException(status_code=404, detail=print('that name is not existing'))
        resp= collection_name.delete_one({'name':name})
        return {'status code': 200, 'meassage': 'userdeleted successfully'}

    except Exception as e:
        return HTTPException(status_code=500, detail=print('some error occurred', e))

app.include_router(router)
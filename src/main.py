from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
 
users = [
    {"id": "1", "name": "Alice", "email": "alice@email.com", "profile": "admin", "status": "ativo"},
    {"id": "2", "name": "Bruno", "email": "bruno@email.com", "profile": "aluno", "status": "inativo"}
]
 
class User(BaseModel):
    name: str
    email: str
    profile: str
    status: str

 
@app.get("/")
def home():
    return {"message": "Wellcome to API SELOEDU"}

 
@app.get("/all_users")
def list_users():
    return users

 
@app.get("/id_user/{id}")
def get_user(id: str):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

 
@app.post("/add_user")
def add_usuario(user: User):
    new_id = str(len(users) + 1)
    new_user = {"id": new_user, **user.dict()}
    users.append(new_user)
    return {"message": "User added successfully", "user": new_user}

 
@app.delete("/delete_user/{id}")
def delete_user(id: str):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": f"User {id} removed successfully"}
    raise HTTPException(status_code=404, detail="User not found")

 
@app.put("/update_user/{id}")
def update_user(id: str, user: User):
    for u in users:
        if u["id"] == id:
            u.update(user.dict())
            return {"message": f"User {id} updated successfully", "user": u}
    raise HTTPException(status_code=404, detail="User not found")

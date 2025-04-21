from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_user, update_user

app = FastAPI()

# Настройки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserUpdate(BaseModel):
    energy: int | None = None
    cash: int | None = None

@app.get("/api/users/{user_id}")
async def read_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users/{user_id}/update")
async def update_user_data(user_id: int, data: UserUpdate):
    return update_user(user_id, **data.dict())
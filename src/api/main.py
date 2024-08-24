from fastapi import FastAPI
from api.routers import users

app = FastAPI()

# ルーターの登録
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

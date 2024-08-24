from fastapi import FastAPI
from api.routers import evacuees, materials, material_details, shelters

app = FastAPI()

# ルーターの登録
app.include_router(evacuees.router)
app.include_router(materials.router)
app.include_router(material_details.router)
app.include_router(shelters.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

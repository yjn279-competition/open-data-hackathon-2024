from fastapi import FastAPI
from api.routers import evacuees, materials, material_details, shelters, ble
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ルーターの登録
# CORSを許可する設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド
    allow_headers=["*"],  # 許可するHTTPヘッダー
)

app.include_router(evacuees.router)
app.include_router(materials.router)
app.include_router(material_details.router)
app.include_router(shelters.router)
app.include_router(ble.router)  # ble ルーターを FastAPI アプリケーションに登録

@app.get("/")
def read_root():
    return {"Hello": "World"}

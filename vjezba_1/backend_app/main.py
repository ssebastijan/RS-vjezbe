from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="RS vjezba 1 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class MenuItem(BaseModel):
    name: str
    price: float


menu: list[dict] = [
    {"id": 1, "name": "Fuzi s tartufima", "price": 14.5},
    {"id": 2, "name": "Crni rižot", "price": 12.0},
    {"id": 3, "name": "Fritule", "price": 5.5},
]


@app.get("/")
def root():
    return {"message": "RS vjezba 1 API is running"}


@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}


@app.get("/jelovnik")
def list_menu():
    return menu


@app.get("/jelovnik/{item_id}")
def get_menu_item(item_id: int):
    for item in menu:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/jelovnik", status_code=201)
def add_menu_item(item: MenuItem):
    new_item = {"id": max((i["id"] for i in menu), default=0) + 1, **item.model_dump()}
    menu.append(new_item)
    return new_item

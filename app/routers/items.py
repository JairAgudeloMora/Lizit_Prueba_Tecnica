from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.services.items_service import create_item, get_items
from app.schemas.items_schemas import ItemCreate, Item

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_new_item(item: ItemCreate):
    return create_item(item)

@router.get("/items/", response_model=List[Item])
def list_items():
    return get_items()

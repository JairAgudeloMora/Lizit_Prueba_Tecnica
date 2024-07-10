from app.repositories.item_repository import create_item_repo, get_items_repo, get_item_by_name
from app.schemas.items_schemas import ItemCreate, Item
from typing import List
from fastapi import HTTPException, status

def create_item(item: ItemCreate) -> Item:
    item.name = item.name.capitalize()

    existing_item = get_item_by_name(item.name)
    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The Item already exists"
        )
    if item.price < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The item's price should be major than 0"
        )
    return create_item_repo(item) 

def get_items() -> List[Item]:
    return get_items_repo()

from sqlalchemy.orm import Session
from app.models.items import Item as DBItem
from app.schemas.items_schemas import ItemCreate, Item
from app.database import SessionLocal
from datetime import datetime, timezone

def create_item_repo(item: ItemCreate) -> Item:
    db_item = DBItem(
        name=item.name,
        price=item.price,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    with SessionLocal() as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

def get_items_repo() -> list[Item]:
    with SessionLocal() as session:
        items = session.query(DBItem).all()
        for item in items:
            if item.created_at is None:
                item.created_at = datetime.now(timezone.utc)
            if item.updated_at is None:
                item.updated_at = datetime.now(timezone.utc)
        return items

def get_item_by_name(name: str) -> DBItem:
    with SessionLocal() as session:
        return session.query(DBItem).filter(DBItem.name == name).first()

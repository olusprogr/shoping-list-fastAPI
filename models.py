from pydantic import BaseModel
import time

class ShopingListItem(BaseModel):
    title: str = "My Shoping Item"
    date: str = time.strftime("%Y-%m-%d %H:%M:%S")
    items: dict[int, dict[str, str]] = {}
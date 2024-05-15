from fastapi import FastAPI
from pydantic import BaseModel

import time


class ShopingList(BaseModel):
    title: str = "My Shoping List"
    date: str = time.strftime("%Y-%m-%d %H:%M:%S")
    items: dict[int, dict[str, str]] = {}

shopingLists: list[ShopingList] = [
    ShopingList(title="My Shoping List", date=time.strftime("%Y-%m-%d %H:%M:%S"), items={1: {"name": "Milk", "quantity": "1L"}}),
    ShopingList(title="My Shoping List 2", date=time.strftime("%Y-%m-%d %H:%M:%S"), items={1: {"name": "Bread", "quantity": "1"}})
]


app = FastAPI()


@app.post("/shopinglist/create/params=")
async def create_list(title: str, date: str):
    for list in shopingLists:
        if list.title == title:
            return {"error": "List with this title already exists"}
        
    list = ShopingList(title=title, date=date)
    shopingLists.append(list)
    return shopingLists

@app.post("/shopinglist/addItems/{shopingListTitle}/items=")
async def add_item(shopingListTitle: str, name: str, quantity: int):
    for list in shopingLists:
        if list.title == shopingListTitle:
            next_item: dict[str, str] = {"name": name, "quantity": quantity}
            next_index: int = max(list.items.keys()) + 1 if list.items else 1
            
            for item in list.items.values():
                if item["name"] == name:
                    return {"error": "Item with this name already exists"}
                
            list.items[next_index] = next_item
            return {"message": "Item added successfully"}

    return {"error": "List with this title does not exist"}

@app.get("/shopinglist/getList/{shopingListTitle}")
async def get_list(shopingListTitle: str):
    for list in shopingLists:
        if list.title == shopingListTitle:
            return list
    return {"error": "List with this title does not exist"}

@app.delete("/shopinglist/deleteList/{shopingListTitle}")
async def delete_list(shopingListTitle: str):
    for list in shopingLists:
        if list.title == shopingListTitle:
            shopingLists.remove(list)
            return {"message": "List deleted successfully"}
    return {"error": "List with this title does not exist"}
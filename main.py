from fastapi import FastAPI, Query, Path
from typing import Annotated, Union, get_type_hints
from models import ShopingListItem
from errorhandlers import *

shopingLists: list[ShopingListItem] = [
    # ShopingList(title="My Shoping List", date=time.strftime("%Y-%m-%d %H:%M:%S"), items={1: {"name": "Milk", "quantity": "1L"}}),
    # ShopingList(title="My Shoping List 2", date=time.strftime("%Y-%m-%d %H:%M:%S"), items={1: {"name": "Bread", "quantity": "1"}})
]


app = FastAPI()

@app.post("/shopinglist/create/newList")
async def create_list(*,
    shopingListItem: ShopingListItem, # example value from models.py
    title: Annotated[str, Query(
        min_length=3,
        max_length=15,
        title="Title of the shoping list"
        )],
    ) -> Union[ShopingListItem, dict[str, str]]:

    for list in shopingLists:
        if list.title == title:
            return {"error": "List with this title already exists"}
        
    shopingListItem.title = title
    shopingLists.append(shopingListItem)
    print(shopingLists)
    return shopingListItem

@app.post("/shopinglist/addItems/{shopingListTitle}/newItems")
async def add_item(
    shopingListTitle: Annotated[str, Query(
        min_length=3,
        max_length=15,
        title="Title of the shoping list"
        )],
    name: str,
    quantity: Annotated[int, Path(title="Quantity of the item", ge=1, le=1000)]
    ) -> dict[str, str]:
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
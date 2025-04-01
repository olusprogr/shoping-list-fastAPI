from fastapi import FastAPI, Query, Path
from typing import Annotated, Union, get_type_hints
from models import ShoppingList
import time
from errorhandlers import *

shoppingLists: list[ShoppingList] = [
    ShoppingList(title="1", date=time.strftime("%Y-%m-%d %H:%M:%S"), items=[{"name": "Milk", "quantity": "1L"}], img={"url": "test.png", "name": "image"}),
    # ShopingList(title="My Shoping List 2", date=time.strftime("%Y-%m-%d %H:%M:%S"), items={1: {"name": "Bread", "quantity": "1"}})
]


app = FastAPI()

@app.post("/shoppinglist/create/newList")
async def create_list(*,
    shopingListItem: ShoppingList, # example value from models.py
    title: Annotated[
        str, Query(
            min_length=3,
            max_length=20,
            title="Title of the shopping list"
        )
    ],
    img: Annotated[
        str, Query(
            min_length=4,
            title="Image data"
        )
    ] = None
    ) -> Union[ShoppingList, dict[str, str]]:
    for list in shoppingLists:
        if list.title == title:
            return {"error": "List with this title already exists"}
        
    shopingListItem.title = title
    shopingListItem.items = []
    shoppingLists.append(shopingListItem)
    print(shoppingLists)
    return shopingListItem

@app.post("/shoppinglist/addItems/{shopingListTitle}/newItems")
async def add_item(*,
    shoppingListItem: ShoppingList,
    shoppingListTitle: Annotated[
        str,
        Query(
            min_length=3,
            max_length=15,
            title="Title of the shopping list"
        )
    ] = "1",
    item: str,
    price: int | None,
    quantity: Annotated[
        int,
        Path(
            title="Quantity of the item",
            ge=1,
            le=1000
        )
    ] = 1
    ):

    for list in shoppingLists:
        if list.title == shoppingListTitle:

            print(list.items)

            """next_item: dict[str, str] = {"name": name, "quantity": quantity}
            next_index: int = max(list.items.keys()) + 1 if list.items else 1
            
            for item in list.items.values():
                if item["name"] == name:
                    return {"error": "Item with this name already exists"}
                
            list.items[next_index] = next_item
            return {"message": "Item added successfully"}"""

    return {"error": "List with this title does not exist"}

@app.get("/shoppinglist/getList/{shopingListTitle}")
async def get_list(shoppingListTitle: str):
    for list in shoppingLists:
        if list.title == shoppingListTitle:
            return list
    return {"error": "List with this title does not exist"}

@app.delete("/shoppinglist/deleteList/{shopingListTitle}")
async def delete_list(shoppingListTitle: str):
    for list in shoppingLists:
        if list.title == shoppingListTitle:
            shoppingLists.remove(list)
            return {"message": "List deleted successfully"}
    return {"error": "List with this title does not exist"}

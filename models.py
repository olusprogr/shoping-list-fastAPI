from pydantic import BaseModel, Field
import time

class Image(BaseModel):
    url: str | None = Field(
        default=None, title="URL of the image"
    )
    name: str = Field(
        default="My Image", title="Name of my image"
    )

class ShoppingListItem(BaseModel):
    amount: int = 1
    item: str = ""
    price: float | None = None

class ShoppingList(BaseModel):
    title: str = Field(
        default="My Shopping List", title="Title of the shopping list", max_length=40
    )
    date: str = Field(
        default=time.strftime("%Y-%m-%d %H:%M:%S"), title="Creation date of your shopping list"
    )
    items: list[ShoppingListItem] = Field(
        default_factory=list, title="List of items in the shopping list"
    )
    img: Image


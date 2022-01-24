from fastapi import FastAPI, Path, HTTPException
import uvicorn
from pydantic import BaseModel


# You just create your fastapi app
app = FastAPI(title="Tutorial", description="1st BigMap AI School")


class Item(BaseModel):
    name: str
    cycle_num: int
    efficiency: float = None


@app.get("/")
def information():
    return {"bigmap": "battery_research"}


@app.get("/info")
def info():
    return {"Data": "AI_school"}


battery_category = {
    1: {"name": "LIBs",
        "cycle_num": 900,
        "efficiency": 85
        }
}


@app.get("/get-battery-cytegory/{item_id}")
def get_item(item_id: int = Path(default=None, description="The ID of the desired category")):
    return battery_category[item_id]


@app.get("/get-by-name")
def get_item(item_id: int, name: str = None):  # query parameter
    for item_id in battery_category:
        if battery_category[item_id]["name"] == name:
            return battery_category[item_id]
        else:
            raise HTTPException(status_code=404)


@app.post("/create-category/{item_id}")
def create_item(item_id: int, item: Item):   # inherit from a class called basedmodel
    if item_id in battery_category:
        return {"Error": "Item ID already exists."}
    battery_category[item_id] = item
    return battery_category[item_id]


@app.put("/update-category/{item_id}")  # update an item
def update_category(item_id: int, name: str):
    if item_id not in battery_category:
        raise HTTPException(status_code=404)
    battery_category[item_id]["name"] = name
    return battery_category[item_id]


@app.delete("/delete_category")
def del_category(item_id: int):
    del battery_category[item_id]
    return battery_category


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
    print("app is started.")

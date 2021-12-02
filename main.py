from typing import List
from fastapi import FastAPI
from src.services import get_trends_from_mongo, save_trends
import uvicorn
from src.responses import TrendItem

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


if __name__ == "__main__":
    trends = get_trends_from_mongo()
    if not trends:
        save_trends()
    uvicorn.run(app, host="127.0.0.1", port=8000)

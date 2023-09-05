import math

from databases import Database
from fastapi import FastAPI, Query

from app.config import DATABASE_URL
from app.models import Weather

app = FastAPI()


database = Database(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/weather")
async def get_weather(
    page: int = Query(1, gt=0, description="Page number"),
    page_size: int = Query(10, gt=0, le=100, description="Items per page"),
):
    query = f"""
        SELECT * FROM weather_table
        ORDER BY timestamp DESC
        OFFSET {(page - 1) * page_size} LIMIT {page_size}
    """
    rows = await database.fetch_all(query=query)
    results = [Weather(**row) for row in rows]

    total_query = "SELECT COUNT(*) FROM weather_table"
    total = await database.fetch_val(query=total_query)
    total_pages = math.ceil(total / page_size)
    
    return {
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size,
        "total_items": total,
        "items": results,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

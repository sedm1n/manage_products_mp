import uvicorn
from fastapi import FastAPI

from app.routers import auth, categories, products

app = FastAPI()


app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

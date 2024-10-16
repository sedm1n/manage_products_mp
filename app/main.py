import uvicorn
from fastapi import FastAPI
from app.routers import categories, products, user



app = FastAPI()


app.include_router(categories.router)
app.include_router(products.router)
app.include_router(user.router)

if __name__ == "__main__":
      uvicorn.run(app, host="localhost", port=8000)
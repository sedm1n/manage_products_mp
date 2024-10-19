import time
import uvicorn
from fastapi import FastAPI

from app.routers import auth, categories, products
from app.logger import logger

app = FastAPI()


app.include_router(categories.router)
app.include_router(products.router)
app.include_router(auth.router)


@app.middleware("http")
async def logging_middleware(request, call_next):
    try:

        response = await call_next(request)
        if request.status_code in [401, 402, 403, 404]:
            logger.warning("Request to %s failed ",request.url_path )
        
    except Exception as e:
        logger.error("Request to %s failed %s",request.url_path, e, exc_info=True)
        
   
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

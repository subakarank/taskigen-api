from fastapi import FastAPI
from routers import router
from middlewares import cors_middleware

app = FastAPI()
cors_middleware.add_cors_middleware(app)
app.include_router(router.main_route)
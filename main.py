from fastapi import FastAPI
from routers import router
from middlewares import cors_middleware, auth_middleware

app = FastAPI()
# Define the routes that require authentication
# protected_routes = [
#     "/me",
# ]

cors_middleware.add_cors_middleware(app)
# app.add_middleware(auth_middleware.AuthenticationMiddleware, enabled_routes = protected_routes )
app.include_router(router.main_route)
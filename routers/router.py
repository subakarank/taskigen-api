from fastapi import APIRouter, Depends
from . import home, login, register, user_router
from middlewares.auth_middleware import AuthenticationMiddleware
main_route = APIRouter()

auth_middleware = AuthenticationMiddleware()
protected_router = APIRouter()
protected_router.include_router(user_router.router)

main_route.include_router(home.router)
main_route.include_router(login.router)
main_route.include_router(register.router)
main_route.include_router(protected_router)





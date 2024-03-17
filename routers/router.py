from fastapi import APIRouter
from . import home, login, register

main_route = APIRouter()

main_route.include_router(home.router)
main_route.include_router(login.router)
main_route.include_router(register.router)





from fastapi import APIRouter, Depends
from . import home, login, register, user_router, project_router, task_router

main_route = APIRouter()

main_route.include_router(home.router)
main_route.include_router(login.router)
main_route.include_router(register.router)
main_route.include_router(user_router.router)
main_route.include_router(project_router.router)
main_route.include_router(task_router.router)





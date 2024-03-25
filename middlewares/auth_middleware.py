from wsgiref.types import WSGIApplication
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.routing import APIRoute
from dependencies.auth import get_authenticated_user

class AuthenticationMiddleware:
    def __init__(self, app, enabled_routes):
        self.app = app
        self.enabled_routes = enabled_routes

    async def __call__(self, scope, receive, send):
        async def asgi(receive, send):
            await self.app(scope, receive, send)
        await asgi(receive, send)

    async def dispatch(self, request: Request, call_next):
        if request.url.path not in self.enabled_routes:
            # If the current route is not in the list of enabled routes,
            # simply call the next middleware or route handler
            response = await call_next(request)
            return response

        # Your authentication logic here
        # For example, check for authentication token in request headers
        get_authenticated_user()
        # If authentication passes, continue to the next middleware or route handler
        response = await call_next(request)
        return response

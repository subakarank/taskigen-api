from fastapi import FastAPI, Request, HTTPException, status

class AuthenticationMiddleware:
  
    async def dispatch(self, request: Request, call_next):
        # Your authentication logic here
        # For example, check for authentication token in request headers
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or not authorization_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

        # If authentication passes, continue to the next middleware or route handler
        response = await call_next(request)
        return response


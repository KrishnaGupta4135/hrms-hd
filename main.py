import uvicorn
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import users_router, feedback_router,dashboard_route
from src.config import APPNAME, VERSION

# Defining the application
app = FastAPI(
    title=APPNAME,
    version=VERSION,
)

# Define allowed origins
origins = [
    "http://localhost:5173",  # Frontend during development
    "http://127.0.0.1:5173",  # Alternate localhost
    "https://maheshcafe.in",
    "https://www.maheshcafe.in",
    "https://ai-interview-bot-03sf.onrender.com",
    "https://interview-bot-rv6t.onrender.com"
    #"http://ec2-3-219-12-193.compute-1.amazonaws.com:5173"
    # "http://ec2-3-219-12-193.compute-1.amazonaws.com",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Including all the routes for the 'users' module
app.include_router(users_router)
app.include_router(feedback_router)
# app.include_router(dashboard_route)

@app.get("/")
def main_function():
    """
    Redirect to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")

@app.post("/token")
def forward_to_login():
    """
    Redirect to token-generation (`/auth/token`). Used to make Auth in Swagger-UI work.
    """
    return RedirectResponse(url="/token")


# @app.get("/api")
# async def read_root():
#     return {"message": "Hello from API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)

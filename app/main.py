
# imports
from fastapi import FastAPI
from routes.profile import profile_router
from routes.health import health_router

app = FastAPI(title="Dev United")

app.include_router(profile_router)
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "Hello, Effiflo!"}


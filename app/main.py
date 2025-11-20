from fastapi import FastAPI
from .routers import users, courses, trails, sensors, auth

app = FastAPI(
    title="WorkMind API",
    description="API do projeto WorkMind - Global Solution FIAP",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(trails.router)
app.include_router(sensors.router)
app.include_router(auth.router)

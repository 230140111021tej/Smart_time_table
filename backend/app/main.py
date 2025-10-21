from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import schedule

app = FastAPI(title="Smart Timetabling API - MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(schedule.router, prefix="/api/schedule", tags=["schedule"])

@app.get("/")
def read_root():
    return {"message": "Smart Timetabling API — running"}

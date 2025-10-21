from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Slot(BaseModel):
    day: str
    start: str
    end: str

class TimetableEntry(BaseModel):
    batch: str
    subject: str
    faculty: str
    room: str
    slot: Slot

@router.get("/demo", response_model=List[TimetableEntry])
def demo_timetable():
    demo = [
        {
            "batch": "BSc-CS-1A",
            "subject": "Data Structures",
            "faculty": "Dr. A. Sharma",
            "room": "Room 101",
            "slot": {"day": "Mon", "start": "09:00", "end": "10:00"},
        },
        {
            "batch": "BSc-CS-1A",
            "subject": "Mathematics",
            "faculty": "Dr. B. Rao",
            "room": "Room 102",
            "slot": {"day": "Mon", "start": "10:00", "end": "11:00"},
        },
    ]
    return demo

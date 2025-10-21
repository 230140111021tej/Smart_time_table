```markdown
# Smart Timetabling — User-friendly MVP

Overview
A web platform to generate conflict-free, optimized class timetables for colleges and universities.

Features
- Secure login (role-based)
- Master data CRUD (rooms, faculties, batches, subjects, timeslots)
- Optimized timetable generation (demo endpoint)
- Calendar UI (read-only, basic)
- CSV/iCal export
- Dockerized for easy local setup

Quick Start
1. Copy .env.example → .env and fill variables.
2. Run `docker-compose up --build`
3. Backend: http://localhost:8000
   - Demo scheduler: GET /api/schedule/demo
4. Frontend: http://localhost:3000

Tech Stack
- Backend: FastAPI (Python)
- Frontend: Next.js + React + TypeScript
- DB: PostgreSQL
- Solver: OR-Tools CP-SAT

Next Steps
- Add authentication
- Add CRUD endpoints
- Connect real scheduler logic
- Build calendar editor
```

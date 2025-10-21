# Smart Timetabling — User-friendly MVP (Private Repo)

Overview
- Web platform to generate conflict-free, optimized class timetables.
- Focus on simplicity: clean calendar UI, drag/drop editing, multi-option generation, CSV/iCal export.

MVP Features
- Auth (role-based)
- Master data CRUD (rooms, faculties, subjects, batches, timeslots)
- OR-Tools scheduler endpoint (demo)
- Calendar UI (read-only) + basic editor
- CSV / iCal export
- Dockerized for easy local setup

Tech Stack (default)
- Frontend: Next.js + React + TypeScript + Tailwind CSS
- Backend: FastAPI (Python)
- DB: PostgreSQL
- Solver: OR-Tools CP-SAT
- Realtime: Redis for future use
- CI: GitHub Actions (added later)

Quick local run (dev)
1. Copy .env.example → .env and fill variables.
2. Start services:
   - docker-compose up --build
3. Backend: http://localhost:8000
   - Demo scheduler: GET /api/schedule/demo
4. Frontend: http://localhost:3000

Next steps after repository is created
- Add authentication and role-based access
- Implement master-data CRUD endpoints + frontend pages
- Improve the scheduler with real constraints and multiple candidate solutions
- Add CSV import wizard and drag/drop calendar editing
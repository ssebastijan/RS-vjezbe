# Backend app

FastAPI REST API.

Local run:

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

Endpoints: `GET /`, `GET /health`, `GET /jelovnik`, `GET /jelovnik/{id}`, `POST /jelovnik`. Docs at `/docs`.

Render settings (Web Service):
- Root directory: `vjezba_1/backend_app`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

Public URL: TODO (fill in after deploy)

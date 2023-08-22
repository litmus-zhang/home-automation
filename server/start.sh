source venv/Scripts/activate

pytest -v
#uvicorn server.app.main:app  --reload
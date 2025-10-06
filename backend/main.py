from fastapi import FastAPI
from backend.agents.startup_agent import launch_startup

app = FastAPI()

@app.post("/launch")
async def launch(form: dict):
    steps = await launch_startup(form)
    return {"steps": steps}

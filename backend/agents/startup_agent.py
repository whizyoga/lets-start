from backend.workflows.startup_workflow import run_workflow

async def launch_startup(form_data):
    return await run_workflow(form_data)

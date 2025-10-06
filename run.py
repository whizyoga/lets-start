import subprocess
subprocess.Popen(["uvicorn", "backend.main:app", "--port", "8000"])
from frontend.dashboard import app
app.run_server(debug=True, port=8050)

import dash
from dash import html, dcc
import requests

app = dash.Dash(__name__, title="Startup Launcher")

app.layout = html.Div([
    html.H2("Agentic Startup Launcher"),
    dcc.Input(id="startup-name", type="text", placeholder="Enter Startup Name"),
    dcc.Dropdown(
        id="founder-role",
        options=[{"label": r, "value": r} for r in ["CEO", "CFO"]],
        placeholder="Select Founder Role"
    ),
    html.Button("Launch Startup", id="launch-btn"),
    html.Div(id="result")
])

@app.callback(
    dash.Output("result", "children"),
    dash.Input("launch-btn", "n_clicks"),
    dash.State("startup-name", "value"),
    dash.State("founder-role", "value")
)
def launch(n, name, role):
    if not n or not name or not role:
        return "Please fill all fields."
    payload = {"name": name, "role": role}
    res = requests.post("http://localhost:8000/launch", json=payload)
    return html.Ul([html.Li(step) for step in res.json()["steps"]])

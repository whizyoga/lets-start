import httpx
from backend.utils.decision_logic import is_ceo, is_cfo

async def run_workflow(form):
    results = []
    async with httpx.AsyncClient() as client:
        if is_ceo(form["role"]):
            r1 = await client.post("http://localhost:8000/mcp/register", json=form)
            r2 = await client.post("http://localhost:8000/mcp/ein", json=form)
            results += [r1.json(), r2.json()]
        if is_cfo(form["role"]):
            r3 = await client.post("http://localhost:8000/mcp/payroll", json=form)
            results.append(r3.json())
        r4 = await client.post("http://localhost:8000/mcp/onboard", json=form)
        r5 = await client.post("http://localhost:8000/mcp/compliance", json=form)
        results += [r4.json(), r5.json()]
    return results

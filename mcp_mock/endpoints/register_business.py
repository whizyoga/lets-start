from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register(form: dict):
    return {"step": f"Registered {form['name']} with Secretary of State"}

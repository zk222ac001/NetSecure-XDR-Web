from fastapi import APIRouter

router = APIRouter()

@router.get("/threats")
def get_threats():
    return [
        {"name": "Trojan.Generic", "level": "CRITICAL"},
        {"name": "Exploit.Kit", "level": "HIGH"},
        {"name": "Botnet.C2", "level": "MEDIUM"},
    ]
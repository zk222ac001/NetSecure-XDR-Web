from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def get_stats():
    return {
        "alerts": 120,
        "devices": 340,
        "threats": 9,
        "vulnerabilities": 27
    }
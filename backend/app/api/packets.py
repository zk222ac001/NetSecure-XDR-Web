from fastapi import APIRouter
router = APIRouter()
packets = []
@router.get("/packets")
def get_packets():
    return packets
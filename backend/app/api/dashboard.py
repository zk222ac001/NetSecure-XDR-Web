from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def dashboard(request: Request):

    stats = {
        "alerts": 153,
        "critical": 7,
        "devices": 287,
        "vulnerabilities": 31
    }

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "stats": stats
        }
    )
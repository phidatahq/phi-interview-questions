from fastapi import APIRouter

from api.utils.dttm import current_datetime_utc_str

status_router = APIRouter(tags=["Status"])


@status_router.get("/health")
async def status_health():
    """Check the health of the API"""

    return {
        "status": "success",
        "router": "status",
        "path": "/health",
        "utc": current_datetime_utc_str(),
    }

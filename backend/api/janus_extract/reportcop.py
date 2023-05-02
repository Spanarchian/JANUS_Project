from fastapi import APIRouter

router = APIRouter(
    prefix="/cop",
    tags=["cop"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    return {"status": {"Janus extract processor":"Operational"}}

@router.get("/live", tags=["cop","live"])
async def cop_now():
    return {"cop": "LIVE"}

@router.get("/history", tags=["cop","history"])
async def cop_history():
    return [{"cop": "HISTORY"}, {"Status": "Actual display at the time"}]


@router.get("/filter", tags=["cop","current"])
async def cop_filter():
    return [{"cop": "FILTER"}, {"Parameters": f"from: {'strt'} - till: {'till'}"}]


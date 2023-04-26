from fastapi import APIRouter

router = APIRouter(
    prefix="/extract",
    tags=["extract"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    return {"status": {"Janus extract processor":"Operational"}}



@router.get("/live", tags=["cip","live"])
async def cip_now():
    return [{"CIP": "LIVE"}]

@router.get("/history", tags=["cip","history"])
async def cip_history():
    return [{"CIP": "HISTORY"}, {"Status": "Actual display at the time"}]


@router.get("/filter", tags=["cip","current"])
async def cip_filter(strt: str, till: str | None = None):
    return [{"CIP": "FILTER"}, {"Parameters": f"from: {strt} - till: {till}"}]


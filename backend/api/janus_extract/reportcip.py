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


@router.get("/cip/live", tags=["cip","live"])
async def cip_now():
    return {"CIP": "LIVE"}


@router.get("/cip/history", tags=["cip","history"])
async def cip_history():
    return [{"CIP": "HISTORY"}, {"Status": "Actual display at the time"}]


@router.get("/cip/filter", tags=["cip","current"])
async def cip_filter():
    return [{"CIP": "FILTER"}, {"Parameters": f"from: {'strt'} - till: {'till'}"}]


from fastapi import APIRouter

router = APIRouter(
    prefix="/sitrep",
    tags=["sitrep"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    return {"status": {"Janus extract processor":"Inteligence"}}


@router.get("/live", tags=["live"])
async def cip_now():
    return {"sitrep": "LIVE"}


@router.get("/history", tags=["cip","history"])
async def cip_history():
    return [{"sitrep": "HISTORY"}, {"Status": "Actual sitrep display at the time"}]


@router.get("/filter", tags=["cip","current"])
async def cip_filter():
    return [{"sitrep": "FILTER"}, {"Parameters": f"from: {'strt'} - till: {'till'}"}]


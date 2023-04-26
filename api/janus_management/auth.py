from fastapi import APIRouter

router = APIRouter(
    prefix="/mngt",
    tags=["mngt"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    return {"status": {"Janus management processor":"Operational"}}


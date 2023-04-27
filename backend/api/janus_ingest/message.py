from fastapi import APIRouter
import uuid

router = APIRouter(
    prefix="/ingest",
    tags=["ingest"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    return {"status": {"Janus ingest processor":"Operational"}}


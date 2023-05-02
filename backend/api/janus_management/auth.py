from fastapi import APIRouter

router = APIRouter(
    prefix="/mngt",
    tags=["mngt"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_root():
    # To Do
    return {"status": {"Janus management processor":"Operational"}}


@router.get("/login")
def login():
    # To Do
    return {"status": "User has logged in"}


@router.get("/logout")
def logout():
    # To Do
    return {"status": "User has logged out"}


@router.get("/forgot")
def forgot():
    # To Do
    return {"status": "Password reset details have been sent to your listed Email."} 


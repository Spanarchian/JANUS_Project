from fastapi import APIRouter
import logging

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

users_list = {
    "u0001" : {"ref": "u0001", "role": "admin", "uname": "Spanarchian", "email":"spanarchian@gmail.com", "loc":"Wales", "pword" : "Pas55word!"},
    "u0002" : {"ref": "u0002", "role": "moderator", "uname": "SouthCoastpy", "email":"southcoastpy@gmail.com", "loc":"England", "pword" : "Pas55word!"},
    "u0003" : {"ref": "u0003", "role": "user", "uname": "Itestedthis1", "email":"itestedthis1@gmail.com", "loc":"Scotland", "pword" : "Pas55word!"},
    "u0004" : {"ref": "u0004", "role": "user", "uname": "QuantumOfHope", "email":"aquantumofhope@gmail.com", "loc":"Ireland", "pword" : "Pas55word!"}
}


@router.get("/all", tags=["users"])
async def read_users():
    return users_list


@router.get("/me", tags=["users"])
async def read_user_me():
    return users_list["u0001"]


@router.get("/ref/{userId}", tags=["users"])
async def read_user_by_ref(userId: str):
    print(f"{userId} is of type {type(userId)}")
    profile = users_list[ userId ]
    print(f"{profile} is of type {type(profile)}")
    return profile

@router.post("/create", tags=["users"])
async def create_user(userProfile):
    print(f"{userProfile} is of type {type(userProfile)}")
    return userProfile

@router.put("/update", tags=["users"])
async def update_user(userProfile):
    print(f"{userProfile} is of type {type(userProfile)}")
    return userProfile
from fastapi import APIRouter, HTTPException

router = APIRouter(
    tags=["Users"],
    prefix="/users",
)


@router.get("/")
async def get_users():
    return ["112", "123", 1]

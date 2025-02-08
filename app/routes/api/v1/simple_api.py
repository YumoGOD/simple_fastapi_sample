from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def response():
    return{
        "message": "ok"
    }
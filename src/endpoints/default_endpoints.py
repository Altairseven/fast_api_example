"""Default Endpoints"""
# pylint: disable=missing-function-docstring
from fastapi import status, APIRouter

defaultEndpoints = APIRouter(prefix="", tags=["Students"])

@defaultEndpoints.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"status": "ok"}

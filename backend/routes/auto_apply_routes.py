from fastapi import APIRouter, HTTPException
from controllers.auto_apply_controller import auto_apply_controller
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter()

class PreferencesRequest(BaseModel):
    keywords: List[str]
    jobFilters: Dict[str, Any]
    applicationSettings: Dict[str, Any]

@router.post("/auto-apply")
async def auto_apply(preferences: PreferencesRequest):
    try:
        result = await auto_apply_controller.auto_apply(preferences.dict())
        if not result.get("success"):
            raise HTTPException(status_code=400, detail=result.get("message"))
        return result
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.get("/history")
async def get_history():
    try:
        result = await auto_apply_controller.get_history()
        return result
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


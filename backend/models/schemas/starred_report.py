from pydantic import BaseModel
from typing import Optional, Dict, Any

class StarredReportModel(BaseModel):
    id: Optional[int]
    title: str
    path: str
    filter_settings: Optional[Dict[str, Any]]

    class Config:
        orm_mode = True

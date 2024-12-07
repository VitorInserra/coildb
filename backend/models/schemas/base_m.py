from pydantic import BaseModel

class LargestIdResponse(BaseModel):
    largest_id: int
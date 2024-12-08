from pydantic import BaseModel

class KeyStatsResponse(BaseModel):
    departments_participating: int
    courses_available: int
    participating_schools: int
    students_enrolled: int

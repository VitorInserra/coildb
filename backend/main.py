from fastapi import FastAPI
from resources.coil_base import CoilBase
import uvicorn

app = FastAPI()

coil_base = CoilBase()
app.include_router(coil_base.get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/endpoints")
def get_endpoints():
    endpoints_list = [
        { "name": "getUsers", "url": "/users", "method": "GET" },
        { "name": "createUser", "url": "/users", "method": "POST" }
    ]
    return JSONResponse(content={"endpoints": endpoints_list})

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import random

app = FastAPI()
counter = 0
x = random.randint(0,1)

@app.get("/")
def root():
    if x == 1:
        return JSONResponse(
        {
            "status" : 200,
            "message": "Hello DevOps World",
            },
    )
    else:
        return JSONResponse(
        {
            "status" : 204,
            "message": "Nill",
            },
    )

@app.get("/count")
def roof():
    global counter
    counter += 1
    return JSONResponse(
        {
            "status" : 201,
            "response" : "Request count is {}.\n".format(str(counter))
        },
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = 2020,
        reload = False,
    )
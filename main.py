from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
counter = 0

@app.get("/")
def root():
    return JSONResponse(
        {
            "status" : 200,
            "message": "Hello DevOps World",
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
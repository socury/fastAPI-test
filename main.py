from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/",
    summary="엔드 포인트1",
    description="설명")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

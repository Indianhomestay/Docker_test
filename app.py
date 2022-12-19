from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def index():
    return "This is the home page"


@app.get("/sum")
async def sum_two_numbers(
    a: int = 10, 
    b: int = 20
    ):
    return f"Sum of {int(a)} and {int(b)} is {int(a) + int(b)}."


if __name__ == "__main__":
    uvicorn.run(app)

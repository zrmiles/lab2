from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def sum(x: int, y: int):
    return x + y

@app.get("/difference")
def difference(x: int, y: int):
    return x - y

@app.get("/multiplication")
def difference(x: int, y: int):
    return x * y

@app.get("/division")
def division(x: int, y: int):
    if y == 0:
        return ("На 0 делить нельзя")
    else:
        return x / y

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hola mundo"}

@app.get("/saludo")
async def saludo():
    return {"message": "saludo en otra pagina"}
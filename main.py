from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def base_get_route():
    return {"message": "hello word"}

@app.post('/get')
async def aiu():
    return {'message' : 'hello'}

@app.delete('/')
async def aiu():
    return {'message' : 'hello'}

@app.put('/')
async def aiu():
    return {'message' : 'hello'}
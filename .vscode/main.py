from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello word"}



@app.get('/get')
async def aiu():
    return {'message' : 'hello'}
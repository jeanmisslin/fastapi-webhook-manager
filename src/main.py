from fastapi import FastAPI


app = FastAPI()

@app.get("/")  # Defines a basic route
def read_root():
    return {"message": "Hello, FastAPI!"}
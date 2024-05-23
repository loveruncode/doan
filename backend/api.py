from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}



@app.get("/profile")
def user_profile():
    return {"name":"Nhatmy"}
from fastapi import FastAPI
from services.data_loader.dal import DataLoader

app = FastAPI()
dal = DataLoader()

@app.get("/healthz")
def healthz():
    return  {"status": "ok"}

@app.get("/data")
def read_data():
    return dal.get_all_data()
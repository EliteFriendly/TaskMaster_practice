from fastapi import FastAPI, UploadFile, File
from uploadTaskRouter import uploadTask
from taskMasterLLM import TaskMasterLLM
import json

app = FastAPI()
app.include_router(uploadTask)


@app.get("/")
def root():
    return {"Main page"}


    


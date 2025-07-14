from fastapi import FastAPI
from task_Llm.upload_task_router import uploadTask

app = FastAPI()
app.include_router(uploadTask)


@app.get("/")
def root():
    return {"Main page"}


    


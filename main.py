from fastapi import FastAPI, UploadFile, File
from uploadTaskRouter import uploadTask
from taskMasterLLM import TaskMasterLLM
import json

app = FastAPI()

app.include_router(uploadTask)


@app.get("/")
def root():

    task = TaskMasterLLM()
    steps = task.getPlan(task="Заправить машину", description="Мне нужно сегодня заправить машину но я не знаю когда это будет лучше всего сделать")
   
    
    print(steps.items())
    return {steps}





@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        file_path = f"test-files/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        
        return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}
    


from fastapi import FastAPI, UploadFile, File, APIRouter
from pydantic import BaseModel, Field
from taskMasterLLM import TaskMasterLLM


taskMasterLLM = TaskMasterLLM()


#Thing which uses to send task and description into a LLM to generate steps to achive the aim
class ReqTaskLLM(BaseModel):
    userID: int = Field(default=...)
    task: str = Field(default=...,description="Цель пользователя")
    description: str = Field(default=...,description="Описание цели пользователя")



uploadTask = APIRouter(prefix = "/api/task_llm",tags=["Отправка цели и описание цели в LLM, для генерации шагов достижения"])


@uploadTask.post("/postTask")
def  sendToChequeInfo(reqTaskLLM: ReqTaskLLM):
    
    plan = taskMasterLLM.getPlan(task=reqTaskLLM.task,description=reqTaskLLM.description)
    
    return plan
 

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from taskMasterLLM import TaskMasterLLM
import os
from jose import jwt

taskMasterLLM = TaskMasterLLM()
uploadTask = APIRouter(prefix = "/api/task_llm",tags=["Отправка цели и описание цели в LLM, для генерации шагов достижения"])



#Thing which uses to send task and description into a LLM to generate steps to achive the aim
class ReqTaskLLM(BaseModel):
    userID: int = Field(default=...)
    task: str = Field(default=...,description="Цель пользователя")
    description: str = Field(default=...,description="Описание цели пользователя")


def tokenVerification(token,userId):
    secretKey = os.getenv("SECRET_KEY")
    try:
        deCode = jwt.decode(token=token, key=secretKey, algorithms="HS256")
        if(deCode!=userId):#?
            raise HTTPException(status_code=401, detail="Invalid token") 
    except Exception:
        raise HTTPException(status_code=401, detail="Expired token")


@uploadTask.post("/postTask")
def  sendToChequeInfo(reqTaskLLM: ReqTaskLLM):
    plan = taskMasterLLM.getPlan(task=reqTaskLLM.task,description=reqTaskLLM.description)
    return plan
 

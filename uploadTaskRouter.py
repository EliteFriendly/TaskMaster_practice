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

#TODO нужно это сделать мидлварой, либо при каждом запросе вызывать,
#   следовательно каждый роут должен наследовать класс с этой функцией
#   Так же тебе нужно будет все настройки моделей вынести либо в models,
#   либо в settings в зависимости от содержимого
def tokenVerification(token,userId):
    #TODO ну нужно настраивать интеграцию с командой, посмотри структуру декодированного токена у них
    secretKey = os.getenv("SECRET_KEY")
    try:
        deCode = jwt.decode(token=token, key=secretKey, algorithms="HS256")
        if(deCode!=userId):#?
            raise HTTPException(status_code=401, detail="Invalid token") 
    except Exception:
        raise HTTPException(status_code=401, detail="Expired token")

#TODO Как и говорил отдельное приложение с одной нейронкой и промтами по ней,
#   там и будет этот роут, не забывай пользоваться классами
@uploadTask.post("/postTask")
def  sendToChequeInfo(reqTaskLLM: ReqTaskLLM):
    plan = taskMasterLLM.getPlan(task=reqTaskLLM.task,description=reqTaskLLM.description)
    return plan
 

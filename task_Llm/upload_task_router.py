from task_Llm.task_master_llm import TaskMasterLLM
from fastapi import APIRouter
import os
from jose import jwt
from input_Protect.validation_input import ReqTaskLLM
from input_Protect.middleware import MiddleWare


taskMasterLLM = TaskMasterLLM()
uploadTask = APIRouter(prefix = "/api/task_llm",tags=["Отправка цели и описание цели в LLM, для генерации шагов достижения"])




#TODO нужно это сделать мидлварой, либо при каждом запросе вызывать,
#   следовательно каждый роут должен наследовать класс с этой функцией
#   Так же тебе нужно будет все настройки моделей вынести либо в models,
#   либо в settings в зависимости от содержимого


#TODO Как и говорил отдельное приложение с одной нейронкой и промтами по ней,
#   там и будет этот роут, не забывай пользоваться классами
@uploadTask.post("/postTask")
def  sendToChequeInfo(reqTaskLLM: ReqTaskLLM):
    plan = taskMasterLLM.getPlan(task=reqTaskLLM.task,description=reqTaskLLM.description)
    return plan
 

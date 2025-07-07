from fastapi import FastAPI, UploadFile, File, APIRouter
from pydantic import BaseModel, Field


#Thing which uses to send info in ChequeInfo
class ReqImgLLM(BaseModel):
    #qrImg: UploadFile = Field(default=...,description="Файл с qr-кодом чека")
    userID: int = Field(default=...)
    qrInfo:str = Field(description="Информация с чека")



uploadTask = APIRouter(prefix = "/api/autofill_llm",tags=["Отправка чека для дальнейшего заполнения в бд"])


@uploadTask.post("/uploadIMG")
def  sendToChequeInfo(reqImgLLM: ReqImgLLM):
    return {"message": "File saved successfully"}
    
@uploadTask.get("/showProductsList")
def getProductList():
    return 0


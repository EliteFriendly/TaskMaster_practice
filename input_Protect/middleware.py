import os
from jose import jwt
from fastapi import HTTPException

class MiddleWare:
    __secretKey = os.getenv("SECRET_KEY")
    def tokenVerification(self,token,userId):
        #TODO ну нужно настраивать интеграцию с командой, посмотри структуру декодированного токена у них
        try:
            deCode = jwt.decode(token=token, key=self.__secretKey, algorithms="HS256")
            if(deCode!=userId):#?
                raise HTTPException(status_code=401, detail="Invalid token") 
            return True
        except Exception:
            raise HTTPException(status_code=401, detail="Expired token")
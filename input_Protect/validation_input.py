from pydantic import BaseModel, Field


#Thing which uses to send task and description into a LLM to generate steps to achive the aim
class ReqTaskLLM(BaseModel):
    userID: int = Field(default=...)
    task: str = Field(default=...,description="Цель пользователя")
    description: str = Field(default=...,description="Описание цели пользователя")

from llama_cpp import Llama
import json


class TaskMasterLLM:
    __llm = Llama.from_pretrained(
       	repo_id="bartowski/Ministral-8B-Instruct-2410-GGUF",
	    filename="Ministral-8B-Instruct-2410-Q4_K_S.gguf",
    )
    
    
    
    def getPlan(self,task,description):
        #TODO Так ну тут тебе советую сделать отдельный файл обработчик промтов,
        #  куда ты будешь записывать messages и может менеджер запонения этих промтов по **kwargs, там я думаю можно и response format оставить.
        response = self.__llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"Ты помогаешь мне составить план для достижения цели, я поставил себе следующую цель на день: <{task}>. \
                    Также сформировал следующее описание, чтобы конкретизировать цель: <{description}>.\
                    На вход поступает моя цель и описание к ней. Я хочу чтобы ты составил шаги к её достижению, но чтобы это можно было сделать за день.\
                                    Я хочу чтобы шаги были понятны и не нужно плодить банальных шагов.\
                        Сохрани в файл типа json. В качестве ответа помести в steps мне массив с элементами типа string - шаги для достижения цели. \
                             В элементах массива используй следующий формат: <номер шага. Описание действия>.\
                            В случае если данная цель является невозможной то в поле category напиши <I>, иначе оставь поле пустым "
                    
            },
        ],
        response_format={
            "type": "json_object",
            "schema": {
                "type": "object",
                "properties": [{"steps":[{"type":"string"}]},{"category":""}],
                "required": ["steps","category"]

            },
        },
        temperature=0.35
        )
        
        return json.loads(response["choices"][0]["message"]["content"])
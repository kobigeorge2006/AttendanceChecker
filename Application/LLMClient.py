class LLMClient:
    def __init__(self,api_key:str, model_name:str):
        self.api_key = api_key
        self.model_name = model_name

    def generateResponse(self, prompt,attendanceContext):
        pass
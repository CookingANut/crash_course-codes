class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """储存一个问题，并为储存答案做准备"""
        self.question = question
        self.response = []
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    
    def store_response(self, new_response):
        """储存单份调查答案"""
        self.response.append(new_response)
    
    def show_result(self):
        """显示收集到的所有答卷"""
        print("Survey result:")
        for response in self.response:
            print('- ' + response)

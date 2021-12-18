class Test_addition:

    def __init__(self, test_case, addition_execution, test_result):
        self.test_case = test_case        
        self.addition_execution = addition_execution        
        self.test_result = test_result        

    def execution(self):        
        if self.addition_execution == self.test_result:
            return f'Test case {self.test_case}  passed'
        else:
            return f'Test case {self.test_case}  NOT passed'


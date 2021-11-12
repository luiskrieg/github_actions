class Test_user:

    def __init__(self, test_case, user_id, test_id):
        self.test_case = test_case
        self.user_id = user_id
        self.test_id = test_id

    def test_id(self):
        if self.user_id == self.test_id:
            return f"Test case {self.test_case} PASSED"
        else:
            return f"Test case {self.test_case} NOT PASSED"
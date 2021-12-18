class User:

    def __init__(self, id, full_name, email, phone):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone = phone


    def get_id(self):
        return self.id
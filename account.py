
class Account:
    company_name = ""
    def __init__(self, company_name):
        self.company_name = company_name

    def get_name(self):
        return self.company_name
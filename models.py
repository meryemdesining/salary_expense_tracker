# models.py

class Salary:
    def __init__(self, employee_id, amount, date):
        self.employee_id = employee_id
        self.amount = amount
        self.date = date

class Expense:
    def __init__(self, employee_id, amount, date):
        self.employee_id = employee_id
        self.amount = amount
        self.date = date

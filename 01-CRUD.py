class Employee :

    def __init__(self, fullname, address, salary, phone) :
        self.fullname = fullname
        self._address = address
        self._salary = salary
        self._phone = phone

    @staticmethod
    def create(data):
        data = [
            s
        ]

employee = Employee()
employee.create({"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"})
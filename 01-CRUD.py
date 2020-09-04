class Employee :
    mydict = {}

    def __init__(self, fullname, address, salary, phone) :
        self._fullname = fullname
        self._address = address
        self._salary = salary
        self._phone = phone

    @staticmethod
    def create(self, data):
        mydict = {
            self._fullname : data['fullname']
            self._address : data['address']
            self._salary : data['salary']
            self._phone : data['phone']
        }

        return mydict
    
    

employee = Employee()
employee.create({"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"})
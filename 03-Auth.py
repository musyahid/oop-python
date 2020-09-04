class Auth:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @staticmethod
    def login(data):
        if data['username'] == "root" and data['password'] == "secret":
            self.__username = data['username']
            self.__password = data['password']
            print('login successfully')
        else : 
            print("username atau password salah")
    
    def validate(data) :
        if data['username'] == '' :
            return false
        elif data['password'] == '':
            return false
        else:
            return true 

    def user(self) :
        return f"username : {self.__username} password : {self.__password}" 

auth = Auth()
auth.login({"username": 'root', "password": 'secret'})
auth.validate({'username': 'root', 'password': 'secret'}) 
auth.user()

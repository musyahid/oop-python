class Auth:
    @staticmethod
    def login(data):
        if data['username'] == "root" and data['password'] == "secret":
            print('oke')
        else : 
            print("username atau passsword salah")

auth = Auth()
auth.login({"username": 'root', "password": 'secret'})
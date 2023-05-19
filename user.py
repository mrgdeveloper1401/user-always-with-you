import hashlib
from uuid import uuid4

class User:
    users_dict = {}
    def __init__(self, username, password, number_phone=None):
        self.username = username
        self.password = User.encrypt_password(password)
        self.number_phone = number_phone
        self.id = str(uuid4())
        
    @staticmethod
    def validate_password(password):
       if len(password) >= 4:
            return True
       else:
           print('Password must be at least 4 characters long.')

    @staticmethod
    def encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, encrypted_password):
        return User.encrypt_password(password) == encrypted_password

    def __str__(self):
        return f"Username: {self.username}\n" \
               f"Phone Number: {self.number_phone}\n" \
               f"User ID: {self.id}"
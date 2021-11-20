from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # password encryption obj

def hash(data):
    return pwd_context.hash(data)
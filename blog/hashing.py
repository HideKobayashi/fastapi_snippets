from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"])


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_context.hash(password)

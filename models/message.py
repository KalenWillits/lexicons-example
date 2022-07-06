from lexicons import Model

from .user import User


class Message(Model):
    user: User
    timestamp: int
    body: str


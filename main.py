from lexicons import Server

from channels.public import Public
from headers.login import Login
from headers.register import Register
from models.message import Message
from models.user import User
from signals.create_chat import CreateChat
from signals.get_chat_list import GetChatList


sv = Server(Public, Login, Register, Message, User, CreateChat, GetChatList)


if __name__ == '__main__':
    sv.run()

from lexicons import Server

from channels.public import Public
from headers.login import Login
from headers.register import Register
from models.message import Message
from models.user import User
from signals.create_chat import CreateChat
from signals.get_chat_list import GetChatList


def on_disconnect(db=None, sv=None, ws=None):
    user = db.get('User', ws.auth)
    payload = {'UserExit': f'{user.username} is now offline...'}
    sv.broadcast(payload, ['Public'])

def on_connect(db=None, sv=None, ws=None):
    user = db.get('User', ws.auth)
    payload = {'UserEnter': f'{user.username} has come online...'}
    sv.broadcast(payload, ['Public'])


sv = Server(Public, Login, Register, Message, User, CreateChat, GetChatList, on_connect=on_connect,
            on_disconnect=on_disconnect)


if __name__ == '__main__':
    sv.run()

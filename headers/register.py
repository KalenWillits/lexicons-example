from lexicons import Header
from lexicons.utils import encrypt


class Register(Header):
    def execute(self, db=None, ws=None, username=None, password=None, **kwargs):
        if db.query('User', username=username).empty:
            user = db.create('User', username=username, password=encrypt(password))
            ws.auth = user.pk

        return False

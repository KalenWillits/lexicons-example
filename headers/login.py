from lexicons import Header
from lexicons.utils import encrypt


class Login(Header):
    def execute(self, db=None, sv=None, ws=None, username=None, password=None, **kwargs):
        user = db.get('User', username=username, password=encrypt(password))
        if user:
            ws.auth = user.pk
            sv.channels['Public'].subscribe(ws.pk)
            return True

        return False

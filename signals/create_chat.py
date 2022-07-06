from datetime import datetime

from lexicons import Signal


class CreateChat(Signal):
    def execute(self, db=None, ws=None, body=None, **kwargs):
        user = db.get('User', ws.auth)
        timestamp = int(datetime.now().timestamp())
        message = db.create('Message', user=user.pk, body=body, timestamp=timestamp)
        payload = message._to_dict()
        payload['username'] = user.username
        return self.reponse(payload, ['Public'])

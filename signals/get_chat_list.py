from lexicons import Signal


class GetChatList(Signal):
    def execute(self, db=None, ws=None, **kwargs):
        message_df = db.query('Message')
        user_df = db.query('User')
        merged_df = db.Message.merge(db.User, how='inner', left_on='user', right_on='pk')
        limited_fields_df = meged_df[['username', 'body', 'timestamp']]
        payload = limited_fields_df.to_dict(orient='records')
        return self.response(payload, [ws.auth])



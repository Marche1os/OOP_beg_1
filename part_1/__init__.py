class User:
    id = 0
    nickname = 'nickname'
    last_activity = 0
    first_name = 'fName'
    last_name = 'lName'

class Message:
    def __init__(self, from_user, to_user, type, description, chat_id):
        self.from_user = from_user
        self.to_user = to_user
        self.type = type
        self.description = description
        self.chat_id = chat_id


class Chat:
    id = 0
    creator: User
    creation_time = 0


my_message = Message("me", "you", "text", "hey kid", 1)
print(my_message.description)
class User:
    def __init__(self, id, nickname, first_name, last_name):
        self.id = id
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name

    def rename_first_name(self, new_first_name):
        self.first_name = new_first_name

    def rename_last_name(self, new_last_name):
        self.last_name = new_last_name

    def rename_nickname(self, new_nickname):
        self.nickname = new_nickname

class Message:
    def __init__(self, from_user, to_user, type, description, chat_id, msg_id):
        self.from_user = from_user
        self.to_user = to_user
        self.type = type
        self.description = description
        self.chat_id = chat_id
        self.msg_id = msg_id

    def edit(self, new_description):
        self.description = new_description

    def replay(self, msg_id, to_user):
        self.to_user = to_user

    # Логика для примера
    def share(self, msg_id):
        self.msg_id = msg_id


class Chat:
    def __init__(self, id, creator, creation_time, is_read, enabled_notification):
        self.id = id
        self.creator = creator
        self.creation_time = creation_time
        self.is_read = is_read
        self.enabled_notification = enabled_notification

    def read(self):
        self.is_read = True

    def unread(self):
        self.is_read = False

    def enable_notification(self):
        self.enabled_notification = True

    def disable_notification(self):
        self.enabled_notification = False


first_message = Message("me", "friend", "text", "My first message", 0, 0)
print(first_message.description) # My first message

first_message.edit("My second message")
print(first_message.description) # My second message

me = User(1, "Marchelos", "Mark", "")
print(me.nickname) # Marchelos
me.rename_nickname("Marche1os")
print(me.nickname) # Marche1os
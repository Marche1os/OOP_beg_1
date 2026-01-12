class User:
    id = 0
    nickname = 'nickname'
    last_activity = 0
    first_name = 'fName'
    last_name = 'lName'

class Message:
    from_user: User
    to_user: User
    type = 'text'
    description = 'description'
    chat_id = 0

class Chat:
    id = 0
    creator: User
    creation_time = 0

user_1 = User()
user_1.nickname = 'Alex'

user_2 = User()
user_2.nickname = 'NotAlex'
user_2 = user_1

print(user_1.nickname)
print(user_2.nickname)
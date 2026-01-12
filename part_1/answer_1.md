### 1.1

За пример возьму приложение Telegram и игру Cyberpunk 2077.
Для мессенджера варианты классов:
- Message, описывающее сообщение. Может включать в себя отправителя, получателя, тип сообщения (голосовое, текстовое и т.д.)
- Чат. Может быть представлено групповым чатом и личным. Содержать список сообщений, иметь тему, аватарку. Также свойство, например, является ли это чат с самим собой

Для игры это могут быть следующие классы:
- Класс автомобиль. Содержит различные свойства, такие как: тип авто, признак, является ли транспорт боевым (содержит ли оружие), максимальная скорость, разгон. Объектами будут конкретные экземпляры авто, которые есть в игровом мире;
- Класс "Игровое задание". По структуре содержит условие получения задания, статус (доступно к выполнению, в прогрессе, выполнено/провалено), действующие лица, связи с другими заданиями...

### 1.2

```python
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

print(user_1.nickname) #Alex
print(user_2.nickname) #NotAlex

```

### 1.3

```python
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

print(user_1.nickname) #Alex
print(user_2.nickname) #Alex
```
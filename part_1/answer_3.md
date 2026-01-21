### 5.1

```python
class User:
    def __init__(self, id, nickname, first_name, last_name):
        self.id = id
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return self.id
    
    def get_nickname(self):
        return self.nickname
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
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

    def get_from_user(self):
        return self.from_user
    
    def get_to_user(self):
        return self.to_user
    
    def get_type(self):
        return self.type
    
    def get_description(self):
        return self.description
    
    def get_chat_id(self):
        return self.chat_id
    
    def get_msg_id(self):
        return self.msg_id
    
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

    def get_id(self):
        return self.id

    def get_creator(self):
        return self.creator
    
    def get_creation_time(self):
        return self.creation_time
    
    def get_is_read(self):
        return self.is_read
    
    def get_enabled_notification(self):
        return self.enabled_notification

    def read(self):
        self.is_read = True

    def unread(self):
        self.is_read = False

    def enable_notification(self):
        self.enabled_notification = True

    def disable_notification(self):
        self.enabled_notification = False

```

### 5.2

```python
class Transport:
    def __init__(self, weight, type):
        self.weight = weight
        self.type = type

class Bus(Transport):
    def __init__(self, doors_are_open, weight, type):
        super().__init__(weight, type)
        self.doors_are_open = doors_are_open

    def open_doors_for_passengers(self):
        self.doors_are_open = True
        
    def close_doors_for_passengers(self):
        self.doors_are_open = False

class SportCar(Transport):
    def __init__(self, max_speed, has_furious, weight, type):
        super().__init__(weight, type)
        self.max_speed = max_speed
        self.current_speed = 0
        self.has_furious = has_furious
    
    def run_to_max_speed(self):
        self.current_speed = self.max_speed
    
    def start_furious_if_has(self):
        if self.has_furious:
            self.current_speed = (self.max_speed * 2)

class Animal:
    def __init__(self, color, weight, speed):
        self.color = color
        self.weight = weight
        self.speed = speed
    
    def move(self, speed_value):
        self.speed = speed_value

class Cat(Animal):
    def __init__(self, crying, color, weight, speed):
        super().__init__(color, weight, speed)
        self.crying = crying
    
    def sound_murr(self):
        self.crying = True
    
    def stop_murring(self):
        self.crying = False

class Dog(Animal):
    def __init__(self, guffing, color, weight, speed):
        super().__init__(color, weight, speed)
        self.guffing = guffing
    
    def sound_guf(self):
        self.guffing = True
        
    def stop_guffing(self):
        self.guffing = False

```

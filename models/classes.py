from .app_model import Pokemon

### Pokemon Object ###

class Pokemon():

    def __init__(self, name, id, img_url):
        self.name = name
        self.id = id
        self.img = img_url

### User Object ###

class User():

    def __init__(self, id):
        self.id = id
    
    def capture_pokemon(self, pool):
        pass



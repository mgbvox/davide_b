class Person:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.parents = []
        self.children = []

    def get_key(self):
        return f'{self.name}_{self.id}'
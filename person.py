class Person:
    def __init__(self, name, parents = dict(), children = dict()):
        self.name = name
        self.id = None
        self.parents = parents
        self.children = children

    def __repr__(self):
        return f'Person({self.name})'

    def greet(self):
        print(f'Hello {self.name}')

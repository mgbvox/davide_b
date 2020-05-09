from person import Person

class DynasticDescent:
    def __init__(self):
        self.tree = dict()
        self.ids = []
        self.next_id = 1

    def add_person(self, person):
        '''
        Adds a person to the family tree.
        :param person: a Person() object
        :return: None
        '''
        # Gives person an ID if they don't have one.
        if not person.id:
            latest_id = self.next_id
            person.id = latest_id
            self.ids.append(latest_id)
            self.next_id += 1

        #Adds them to the tree if they're not already in the tree:
        tree_key = f'{person.name}_{person.id}'
        if not tree_key in self.tree:
            self.tree[tree_key] = person
            print(f'Added {person.name.upper()} to the family tree!')
        else:
            print(f'{person.name} is already in the tree! Key: {tree_key}')

    def add_child(self, parent, child):
        '''
        :param parent:
        :param child:
        :return:
        '''

        '''
        What's happens if two people in the tree have the same name?
        '''

        #Make sure parent and child are both in tree


        #get parent and child objects from tree


        #add parent to child's parent list, and child to parent's child list.

        pass

    def add_parent(self, child, parent):
        pass


if __name__ == "__main__":
    matt = Person('Matt')
    davide = Person('Davide')

    tree = DynasticDescent()

    tree.add_person(matt)
    tree.add_person(matt)
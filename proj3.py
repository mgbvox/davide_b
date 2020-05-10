from person import Person

class DynasticDescent:
    def __init__(self):
        self.tree = dict()
        self.ids = []
        self.next_id = 1

    def add(self):
        name = str(input('What is the name of the human?'))
        self.add_person(Person(name))

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
        tree_key = person.get_key()
        if not tree_key in self.tree:
            self.tree[tree_key] = person
            print(f'Added {person.name.upper()} to the family tree!')
        else:
            print(f'{person.name} is already in the tree! Key: {tree_key}')

    def ensure_in_tree(self, person):
        if person.get_key() not in self.tree:
            print(f'{person.name} not in tree; adding!')
            self.add_person(person)
        else:
            print(f'{person.name} in tree! Good job!')

    def lookup(self, name):
        matches = []
        for name_key in self.tree.keys():
            if name.upper() in name_key.upper():
                matches.append(name_key)
        if len(matches) == 0:
            print(f'{name} not in tree yet; making a new person (Happy Birthday Person!)')
            new_person = Person(name)
            self.add_person(new_person)
            return new_person
        elif len(matches) == 1:
            #Just return the matching person obj.
            return self.tree[matches[0]]
        elif len(matches) > 1:
            #User needs to pick a person!
            print("Found more than one match, here's the list:")
            print(matches)
            choice = str(input('Which ID do you choose?'))
            chosen_key = f'{name.title()}_{choice}'
            return self.tree[chosen_key]

    def relate(self, parent_name = None, child_name = None, parent = None, child = None):
        '''
        Adds a child to a parent Person object.
        :param parent: a Person object.
        :param child: a Person object.
        :return: None
        '''
        if not parent_name and not parent:
            parent_name = str(input("What is the name of the parent human? "))
        if not child_name and not child:
            child_name = str(input("What is the name of the child human? "))

        if not parent:
            parent = self.lookup(parent_name)
        if not child:
            child = self.lookup(child_name)

        '''
        What happens if two people in the tree have the same name?
        '''

        if (parent and child):

            #Make sure parent and child are both in tree
            self.ensure_in_tree(parent)
            self.ensure_in_tree(child)

            #add parent to child's parent list, and child to parent's child list.
            # parents = {'parent_id' : [parent_1, parent_2, ....]}

            # Matt -> 'Matt_1'
            child.parents.append(parent.get_key())
            parent.children.append(child.get_key())

    def get_ancestors(self, person, degree, depth = 0):
        if depth == degree:
            return [person.name]
        else:
            ancestors = []
            parents = person.parents
            for parent_key in parents:
                parent = self.lookup(parent_key)
                ancestors += self.get_ancestors(parent,degree,depth=depth+1)
            return ancestors



if __name__ == "__main__":
    tree = DynasticDescent()
    user_input = ''
    while user_input != 'quit':
        user_input = str(input('What would you like to do next? '))
        if user_input == 'add':
            tree.add()
        elif user_input == 'relate':
            tree.relate()

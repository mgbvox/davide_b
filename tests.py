from proj3 import DynasticDescent
from person import Person


def test_get_ancestors():
    matt = Person('Matt')
    davide = Person('Davide')
    harold = Person('Harold')
    dd = DynasticDescent()

    dd.relate(parent=matt, child=davide)
    dd.relate(parent=harold, child=matt)

    print(dd.get_ancestors(matt,1))

    print(dd.get_ancestors(davide, 1))
    print(dd.get_ancestors(davide, 2))

if __name__ == "__main__":
    test_get_ancestors()
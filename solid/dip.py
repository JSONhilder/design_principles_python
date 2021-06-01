'''
Design Prinicples were introduced by Robert C. Martin
SOLID is just a selection of 5 principles of many many others.
These are frequently refered to in modern programming &
apply directly to design patterns

Dependency Inversion Principle
(Does not relate to dependency injection)
High level classes /modules should not depend on low level modules but 
rather depend on abstractions.
'''
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Relationships:
    def __init__(self) -> None:
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

#high level module
class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
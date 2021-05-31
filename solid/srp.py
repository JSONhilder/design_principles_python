'''
Design Prinicples were introduced by Robert C. Martin
SOLID is just a selection of 5 principles of many many others.
These are frequently refered to in modern programming &
apply directly to design patterns

SRP(Single Responsibility Principle) - SOC(Seperation of Concerns):
If you have a class, it should have its primary responsibility and not 
take on any other responsibilities.
'''

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    
    def __str__(self) -> str: # Human readable representation of all entries
        return '\n'.join(self.entries)

  
    '''
    All of the above, srp/soc has been maintained ( add and remove entries )
    Lets break that.
    
    All of the below is a secondary responsibility by taking on persistence
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass
    
    It would be wiser to seperate in its own class
    '''

# This is enforcing seperation of concerns
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I bought a chicken mayo toastie boooi')
j.add_entry('I lost the chicken mayo')
print(f'Journal entries:\n{j}')

file = './journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
from Label import Label
from Person import Person
#from Person_singleton import Person
#from Label_singleton import Label

def main():
    people = [
        Person(Label("Alice"), Label("alice@example.com")),
        Person(Label("Bobby"), Label("bobby@example.com")),
        Person(Label("Chris"))  # No email - will use NullLabel
    ]
    
    for person in people:
        print(person)
        person.display()
        print()

if __name__ == "__main__":
    main()

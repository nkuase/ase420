from Person import Person
from Label import Label

def main():
    people = [
        Person(Label("Alice"), Label("alice@example.com")),
        Person(Label("Bobby"), Label("bobby@example.com")),
        Person(Label("Chris"))  # No email
    ]
    
    for person in people:
        print(person)
        person.display()
        print()

if __name__ == "__main__":
    main()

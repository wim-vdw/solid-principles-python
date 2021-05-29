"""
After implementation of SRP (Single Responsibility Principle).

There is high cohesion now between the methods of the different classes and loose coupling
in the classes responsible for printing and saving.
"""


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_full_name(self):
        return self.get_last_name() + ', ' + self.get_first_name()

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name


class Printer:
    def print(self, person: Person):
        pass


class PrintPlaintText(Printer):
    def print(self, person: Person):
        print(person.get_full_name())


class PrintHTML(Printer):
    def print(self, person: Person):
        print(f'<html><body><h1>{person.get_full_name()}</h1></body></html>')


class PersistPerson:
    def save(self, person: Person):
        pass


class PersistPersonFile(PersistPerson):
    def save(self, person: Person):
        with open('data.txt', 'w') as writer:
            writer.write(person.get_full_name())


class PersistPersonDatabase(PersistPerson):
    def save(self, person: Person):
        """Code can be put here to persist person in a database."""
        pass


if __name__ == '__main__':
    person = Person('Wim', 'Van den Wyngaert')
    plain_text_print = PrintPlaintText()
    plain_text_print.print(person)
    html_print = PrintHTML()
    html_print.print(person)
    persist_person_in_file = PersistPersonFile()
    persist_person_in_file.save(person)

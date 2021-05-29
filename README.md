# SOLID principles with Python examples.

In object-oriented computer programming SOLID is a mnemonic acronym for five design principles intended to make software
designs more understandable, flexible, and maintainable.  
The five SOLID design principles are:

* SRP: Single Responsibility Principle
* OCP: Open/Closed Principle
* LSP: Liskov Substitution Principle
* ISP: Interface Segregation Principle
* DIP: Dependency Inversion Principle

## SRP: Single Responsibility Principle

Every software component should have one and only one responsibility or should have only one reason to change.
> Aim for high cohesion and loose coupling.

Cohesion is the degree to which the various parts of a software component are related.  
Coupling is defined as the level of inter-dependency between various software components.

* [Python code before SRP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/01-srp/01-srp-1-before.py)
* [Python code after SRP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/01-srp/01-srp-2-after.py)

## OCP: Open/Closed Principle

Software entities (components) should be closed for modification but open for extension.  
Open closed principle often requires decoupling, which in turn, automatically follows the single responsibility
principle.

* [Python code before OCP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/02-ocp/02-ocp-1-before.py)
* [Python code after OCP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/02-ocp/02-ocp-2-after.py)

## LSP: Liskov Substitution Principle

Objects should be replaceable with their subtypes without affecting the correctness of the program. Functions that use
pointers or references to base classes must be able to use objects of derived classes without knowing it.

## ISP: Interface Segregation Principle

Many client-specific interfaces are better than one general-purpose interface. A client should never be forced to
implement an interface that it does not use or clients should not be forced to depend on methods they do not use.

## DIP: Dependency Inversion Principle

Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the
low-level module, but they should depend on abstractions.

## Task list

- [x] Update general information on what SOLID is.
- [x] Document SRP principle including code examples.
- [x] Document OCP principle including code examples.
- [ ] Document LSP principle including code examples.
- [ ] Document ISP principle including code examples.
- [ ] Document DIP principle including code examples.
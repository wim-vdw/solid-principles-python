# SOLID principles with Python examples.

## SRP: Single Responsibility Principle

Every software component should have one and only one responsibility or should have only one reason to change.
> Aim for high cohesion and loose coupling.

Cohesion is the degree to which the various parts of a software component are related.  
Coupling is defined as the level of inter-dependency between various software components.

* [Python code before SRP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/01-srp/01-srp-1-before.py)
* [Python code after SRP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/01-srp/01-srp-2-after.py)

## OCP: Open/Closed Principle

Software components should be closed for modification but open for extension.  
Open closed principle often requires decoupling, which in turn, automatically follows the single responsibility
principle.

* [Python code before OCP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/02-ocp/02-ocp-1-before.py)
* [Python code after OCP implementation](https://github.com/wim-vdw/solid-principles-python/blob/main/02-ocp/02-ocp-2-after.py)

## LSP: Liskov Substitution Principle

Objects should be replaceable with their subtypes without affecting the correctness of the program.

## ISP: Interface Segregation Principle

No client should be forced to depend on methods it does note use.

## DIP: Dependency Inversion Principle

High-level modules should not depend on low-level modules. Both should depend on abstractions.  
Abstractions should not depend on details. Details should depend on abstractions.

## Task list

- [ ] Update general information on what SOLID is.
- [x] Document SRP principle including code examples.
- [x] Document OCP principle including code examples.
- [ ] Document LSP principle including code examples.
- [ ] Document ISP principle including code examples.
- [ ] Document DIP principle including code examples.
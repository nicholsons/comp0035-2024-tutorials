# 1. Introduction to application design

## Design principles

This is covered further in the lecture notes with references for more information in the reading list.

- KISS: prefer simple to complex. Follow standards that make code easier to read. Deconstruct problems into smaller
  ones; give each function one thing to do. Use the least complex algorithm, data structure etc.
- DRY: do not repeat business logic; some code may be repeated if it relates to different business logic.
- Loose coupling: Coupling is the degree of interdependence between software modules. Keep dependencies between
  modules/classes to the minimum needed.
- High cohesion: Cohesion is the degree to how strongly related and focused are the various responsibilities of a
  module; and how they work together to create something more valuable than the individual parts. Suggestions to
  increase cohesion:
    - The functionalities embedded in a class, accessed through its methods, have much in common.
    - Methods carry out a small number of related activities, by avoiding coarsely grained or unrelated sets of data.
    - Related methods are in the same source file or otherwise grouped together; for example, in separate files but in
      the same subdirectory/folder.
- Separation of concerns: A design principle for separating an application into distinct sections such that each section
  addresses a separate concern. A concern is a set of information that affects the code of a computer program.
- Modular: separate code into modules. The functions within a module should be cohesive. Modules should be loosely
  coupled.

There are many more sets of principles such as SOLID, GRASP if you want to try and apply these!

Many of the principles relate to object-oriented design. While your design will have some classes (objects), they will
also have many functions that do not belong to a class. In Python, functions may be grouped in modules.

## Design patterns

One way to follow these principles in your application's design is to apply relevant design patterns.

A design pattern is a general blueprint to solve a common problem. First documented as design patterns in the
book [Design Patterns: Elements of Reusable Object-Oriented Software in 1994](https://en.wikipedia.org/wiki/Design_Patterns).

There are now many patterns, and you can find Python specific examples, for example
at [Refactoring Guru](https://refactoring.guru/design-patterns/python).

Some of the patterns that may be relevant to your coursework:

- Model view controller (MVC): application design pattern for apps with a user interface that separates business logic
  and views from the underlying data.
  This [Real Python tutorial](https://realpython.com/lego-model-view-controller-python/) explains MVC using Python.
- REST (or RESTful) API: REpresentational State Transfer (REST) was first discussed by Roy Fielding. This is a software
  architecture style for client and server communications using HTTP. REST APIs are often used to access data as web
  service. This [Real Python tutorial](https://realpython.com/api-integration-in-python/) gives an explanation of Python
  REST APIs.
- Object relational mapper (ORM): An [ORM](https://www.fullstackpython.com/object-relational-mappers-orms.html) provides
  an abstraction that maps Python classes to relational database tables. SQLAlchemy follows the ORM pattern and will be
  used in COMP0034.

The Reading list has further links. There is plenty of information online and in the UCL library.

## Documenting the application design

[UML class diagrams](https://realpython.com/lessons/uml-diagrams/) are often used to document the application design.
Most examples of class diagrams assume an object-oriented design. Given you only have 1 lecture and this tutorial on
application design, you are not expected to understand object-oriented design.

For this course, you are asked to design the structure of your app considering:

- Python packages
- Python modules
- Python function
- Python classes

### Tools for diagrams

Mermaid is used in the course materials. There are also online tools such as LucidChart, though this requires you to 
create an account and the free version limits the number of diagrams you can create.

For apps that have already been written, you can generate a UML diagram from the code.
See [PyCharm UML class diagrams](https://www.jetbrains.com/help/pycharm/class-diagram.html) or search for
a [VS Code extension](https://marketplace.visualstudio.com/search?term=UML&target=VSCode&category=All%20categories&sortBy=Relevance).

If your app follows a REST API design, there are specific REST API design tools:

- [Apiary - integrates with GitHub](https://apiary.io/how-apiary-works)
- [Swagger - complies with the OpenAPI standard](https://swagger.io)
- [RAML](https://raml.org/developers/design-your-api)
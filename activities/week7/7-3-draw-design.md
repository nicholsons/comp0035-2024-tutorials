# 3. Draw design

## Select the diagram format

In this activity, we will use the UML class diagram, though may not fully adhere to this.

Mermaid is used as you should have installed this in order to view the activities.

You can draw the diagram on paper instead which may be easier as you won't have to learn the Mermaid syntax to do so.

Remember the following symbols for classes and relationships:

![UML class diagram notation](../img/uml-class-diag-notation.png)

## Add the model classes

The following were derived from the ERD and the activities to identify classes from the user stories.

```mermaid
classDiagram
    class Event {
        String type
        int year
        date start
        date end
        int duration
        int countries
        int events
        int sports
        String highlights
        String url
    }

    class Host {
        String host_name
    }

    class HostEvent {
        <<Association>>
    }

    class Country {
        String country_code
        String country_name
    }

    class Disability {
        String category
    }

    class Participants {
        int participants_m
        int participants_f
        int participants
    }

    class DisabilityEvent {
        <<Association>>
    }

    class Student {
        String first_name
        String last_name
    }

    class Teacher

    class Chart {
        String chart_type
        List~Participants~ participants_data
        List~Event~ event_data
    }

    class Quiz {
        String name
    }

    class Question {
        String question_type
        String question_text
    }

    class AnswerChoice {
        Question question
        String answer_text
        boolean is_correct_answer
        int score_value
    }

    class Response {
        List~Answer~ answers
        Student student
        int score
    }

    Teacher -- Quiz
    Teacher -- AnswerChoice
    Teacher -- Question
    Student -- Response
    Response -- AnswerChoice
    Chart -- Event
    Chart -- Participants
    Quiz -- Question
    Question -- AnswerChoice
    Event -- HostEvent
    Disability -- DisabilityEvent
    Event -- DisabilityEvent
    Host -- HostEvent
    Host -- Country
    Participants -- Event
```    

## Add the controller classes

These control the business logic. I have grouped them according to function, you may choose a different way to group
them. There is no single way to design these!

If not following the MVC model, these operations may be in the relevant model classes.

The logic to create, read, update and delete any of the model classes will be handled by the ORM so have not been added
here. You can add them to the class diagram if you prefer.

```mermaid
classDiagram
    class QuizController {
        Quiz quiz
        Question question
        AnswerChoice answer
        generate_quiz()
        submit_student_resonses()
        generate_student_score()
    }

    class AuthenticationController {
        boolean is_authenticated
        sign_in()
        sign_out()
    }

    class ChartController {
        Filter filter
        generate_filter_values()
        create_line_chart(List filters)
        create_bar_chart(List filers)
        create_map()
    }
```

## Add all the classes to the class diagram and add the relationships

The 'view' classes have been omitted in the diagram below. In the coursework you have represented these with the
wireframes.

You may not agree with this diagram, you may have made different choices to structure it differently.

This version also groups the Python classes into Python packages. This is not required.

```mermaid
classDiagram
    namespace ParalympicsPackage {
        class Event {
            String type
            int year
            date start
            date end
            int duration
            int countries
            int events
            int sports
            String highlights
            String url
        }

        class Host {
            String host_name
        }

        class HostEvent {
            <<Association>>
        }

        class Country {
            String country_code
            String country_name
        }

        class Disability {
            String category
        }

        class Participants {
            int participants_m
            int participants_f
            int participants
        }

        class DisabilityEvent {
            <<Association>>
        }
    }

    namespace AuthenticationPackage {
        class Student {
            String first_name
            String last_name
        }

        class Teacher {
            boolean is_authenticated
        }

        class AuthenticationController {
            Teacher teacher
            verify_authentication(Teacher teacher)
        }
    }

    namespace ChartPackage {
        class Chart {
            String chart_type
            List~Participants~ participants_data
            List~Event~ event_data
        }

        class Filter {
            List~date~ date_range_filter
            String type_filter
        }

        class ChartController {
            Filter filter
            Chart chart
            generate_filter_values()
            create_line_chart(List filters)
            create_bar_chart(List filers)
            create_map()
        }
    }

    namespace QuizPackage {
        class Quiz {
            String name
        }

        class Question {
            String question_type
            String question_text
        }

        class AnswerChoice {
            Question question
            String answer_text
            boolean is_correct_answer
            int score_value
        }

        class Response {
            List~AnswerChoice~ answers
            Student student
            int score
        }

        class QuizController {
            Quiz quiz
            List~Question~ questions
            List~AnswerChoice~ answers
            List~Response~ student_responses
            int score
            generate_quiz()
            generate_student_score(responses)
        }
    }

    Teacher -- Quiz
    Teacher -- AnswerChoice
    Teacher -- Question
    Student -- Response
    Response -- AnswerChoice
    Chart -- Event
    Chart -- Participants
    Quiz -- Question
    Question -- AnswerChoice
    Event -- HostEvent
    Disability -- DisabilityEvent
    Event -- DisabilityEvent
    Host -- HostEvent
    Host -- Country
    Participants -- Event
    QuizController -- Quiz
    QuizController -- Question
    QuizController -- AnswerChoice
    QuizController -- Response
    ChartController -- Chart
    ChartController -- Filter
    AuthenticationController -- Teacher
```    

[Next activity](7-4-review-design.md)
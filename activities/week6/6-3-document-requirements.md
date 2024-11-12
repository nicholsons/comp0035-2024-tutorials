# 3. Document requirements

## Approaches to documenting requirements

Select a structure to formally record the requirements. The two options likely to be of most use for this
course are:

- User stories
- Functional and non-function requirements

Consider if there is a format that better suite the nature of your project/product. For example, User Stories would be
expected if you are following an overall Agile approach to the project.

### User story format

Most agile methods use the user story format.

The basic user story template is:

**As a `_role_`, I want `_goal_` so that `_benefit_`.**

Acceptance criteria, or tests, are often added to the user story to clarify the definition. This is one way of adding
non-functional requirements (or 'constraints') to user stories.

For example:
<hr>
As a website user, I want search functionality to be available on all pages so that I can search for books using keywords.

Acceptance criteria:

1. Search box should accept alphanumeric values
2. Search results should display 10 items per page
3. System responds to all search requests within 2 seconds of receiving the request

<hr>

User stories are not typically classified as functional/non-functional. In some cases the non-functional requirements
may be covered by the acceptance criteria; other times you will
see [user stories written for the non-functional needs](https://www.mountaingoatsoftware.com/blog/non-functional-requirements-as-user-stories)
such as:

> "As a customer, I want to be able to run your product on all versions of Windows from Windows 95 on."

### Functional and non-functional requirements

![Natural language specification](/Users/sarahsanders/PycharmProjects/comp0034-5/docs/assets/img/nat_lang_spec.png)

Each requirement should focus on a single distinct feature or behaviour and should be written in the same uniform
sentence structure. They should not be too vague or abstract; too general or imprecise; or include implementation
information. e.g. "32 The ATM system shall validate the PIN"

You will typically see these listed in a table format, and they may be grouped in some way e.g.

![Functional requirements](/Users/sarahsanders/PycharmProjects/comp0034-5/docs/assets/img/functional.png)

![Non functional requirements](/Users/sarahsanders/PycharmProjects/comp0034-5/docs/assets/img/nonfunctional.png)

## Document the quiz app requirements as user stories

The following is a potential list of user stories for the quiz app based on the mindmap.

| Ref | User story                                                                                                                                                                                        | MoSCoW Categorisation |
|:----|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| 1.  | As a system administrator I want to make updates to the paralympic games database so that the data remains accurate and up to date.                                                               |                       |
| 2.  | As a system administrator, I want to make sure that only a teacher can edit questions and quizzes, and access student scores.                                                                     |                       |
| 3.  | As a student I want to browse information about paralympic games so that I can see what is available.                                                                                             |                       |
| 4.  | As a student I want to search for information so that I can answer quiz questions.                                                                                                                |                       |
| 5.  | As a student I want to view statistical information about the paralympics for each event and across events so that I can find information for my project.                                         |                       |
| 6.  | As a student I want to see charts that show trends over time in the events data and be able to narrow the charts to specific fields or date ranges so that I can find information for my project. |                       |
| 7.  | As a student I want to complete a quiz so that I can assess my learning.                                                                                                                          |                       |
| 8.  | As a student I want to submit my quiz score so that I can participate in the competition to see who scores the highest.                                                                           |                       |
| 9.  | As a teacher I want to add and edit questions so that these can be added to quizes.                                                                                                               |                       |
| 10. | As a teacher I want to add and edit quizzes, including adding questions to them, so that I can offer my students formative assessment.                                                            |                       |
| 11. | As a teacher I want to access students' scores to see which student gained the highest score.                                                                                                     |                       |
| 12. | As a student or teacher I want to be able to access the quiz app from a PC or mobile phone so that I can work at home or in school.                                                               |                       |
| 13. | As a student or teacher I want to be able to use the app through a web browser so that I do not have to install an application on my device.                                                      |                       |

> Activity: write user stories for the medal standings app.

## Adding detail to user stories

User stories are typically written with just enough detail and act as placeholders for later conversations.

Detail may be added following these conversations, usually just before the 'sprint' or 'iteration' in which the user
story will be developed. Such detail is also likely to be useful when you later start testing.

This further detail can be added using 'acceptance criteria' or 'constraints' to the user story.

> Activity: Add detail to a few of the following user stories.

| Ref | User story                                                                                                                                                                                        | Constraints                                                                                                                                                                                                                                                     |
|:----|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | As a system administrator I want to make updates to the paralympic games database so that the data remains accurate and up to date.                                                               | Updates will be requested once per day. A request will be triggered in the quiz app and will use the paralympics API to look for changes since the last date of update.<br>Any changes will be updated in the database.<br>The last update date will be stored. |
| 2.  | As a system administrator, I want to make sure that only a teacher can edit questions and quizzes, and access student scores.                                                                     | Authentication must use the school's single sign on method.                                                                                                                                                                                                     |
| 3.  | As a student I want to browse information about paralympic games so that I can see what is available.                                                                                             |                                                                                                                                                                                                                                                                 |
| 4.  | As a student I want to search for information so that I can answer quiz questions.                                                                                                                |                                                                                                                                                                                                                                                                 |
| 5.  | As a student I want to view statistical information about the paralympics for each event and across events so that I can find information for my project.                                         |                                                                                                                                                                                                                                                                 |
| 6.  | As a student I want to see charts that show trends over time in the events data and be able to narrow the charts to specific fields or date ranges so that I can find information for my project. |                                                                                                                                                                                                                                                                 |
| 7.  | As a student I want to complete a quiz so that I can assess my learning.                                                                                                                          |                                                                                                                                                                                                                                                                 |
| 8.  | As a student I want to submit my quiz score so that I can participate in the competition to see who scores the highest.                                                                           |                                                                                                                                                                                                                                                                 |
| 9.  | As a teacher I want to add and edit questions so that these can be added to quizes.                                                                                                               |                                                                                                                                                                                                                                                                 |
| 10. | As a teacher I want to add and edit quizzes, including adding questions to them, so that I can offer my students formative assessment.                                                            |                                                                                                                                                                                                                                                                 |
| 11. | As a teacher I want to access students' scores to see which student gained the highest score.                                                                                                     |                                                                                                                                                                                                                                                                 |
| 12. | As a student or teacher I want to be able to access the quiz app from a PC or mobile phone so that I can work at home or in school.                                                               |                                                                                                                                                                                                                                                                 |
| 13. | As a student or teacher I want to be able to use the app through a web browser so that I do not have to install an application on my device.                                                      |                                                                                                                                                                                                                                                                 |

[Next activity](6-4-prioritise-requirements.md)
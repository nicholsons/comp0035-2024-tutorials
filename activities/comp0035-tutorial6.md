# COMP0035 Tutorial 6: Requirements and Wireframes

There is no coding in this session. The paralympics project examples is continued to give the opportunity to practice in
documenting requirements; creating wireframes and designing an application.

Please note that the example is less substantial than you will produce for your coursework so do not use it as an
exemplar. It is not an example of the final coursework, only a learning activity to learn how to apply techniques.

## Dashboard web app: Product and target audience

The web app to be designed is a dashboard with data visualisations based on paralympic events data.

The target audience is college students who will use the dashboard to gain insights into the paralympics for a school
project in which they have to write a report about the paralympics.

The questions that they have been asked to answer are:

- How has the number of male and female competitors in the paralympics changed over time?
- Does the ratio of male:female competitors vary between winter and summer olympics?
- Where have the paralympics been held?

Make the following assumptions:

- the target audience is familiar with web app technology
- the target audience is not familiar with using dashboards or interpreting data
- the target audience will mostly use a mobile phone to access the dashboard

The dataset contains the following fields with an example entry:

- Host city: Tokyo 
- Year: 1964 
- Country: Japan 
- Type: Summer 
- Start: 1964-11-08 
- End: 1964-11-12 
- Participants (M): 195.0 (total male participants)
- Participants (F): 71.0 (total male participants)
- Participants: 266 (total participants) 
- NOC: JPN (3-letter code representing the region)
- Duration: 4 (number of days the event lasted)

## Document user stories

A brainstorming activity resulted in the following notes:

- No login
- Must work on Android and OSX phones
- Web page is displayed portrait
- Only show one chart at a time to avoid confusion and also the screen is quite small
- Maybe some kind of drop-down to select the question they want to answer first?
- Show the event locations as a map, let them click on location markers to see event data
- Let them select male, female or total participants and display the trends over time
- Let them select winter, summer or both events and display the % female and % male participants

From the notes above, document 2-3 requirements using the user stories format.

> Challenge yourself: Can you add any success criteria?

Refer to the [requirements guide](https://nicholsons.github.io/comp0034-5/guide/requirements.html#user-story-format) or
other sources for examples of the user story format.

## Design a wireframe

> As a college student, I want to be able to select charts that will help me to answer a specific question so that I am supported to find what I need.
>
> Acceptance criteria:
> 1. Must at least support the questions given in the assignment (How has the number of male and female competitors in the paralympics changed over time? Does the ratio of male:female competitors vary between winter and summer olympics? Where have the paralympics been held?)
> 2. Must display on a mobile phone 

Design a wireframe for the above user story.

Refer to the [wireframes guide](https://nicholsons.github.io/comp0034-5/guide/wireframes.html) for examples of how to create a wireframe. There are also references in the [reading list](https://moodle.ucl.ac.uk/mod/lti/view.php?id=4787472).
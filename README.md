# COMP0035 2024-25 Computer practicals

This repository contains the practicals for the COMP0035 module for the academic year 2024-25.

## Instructions for using this repository

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine (e.g. in VS Code or PyCharm).
3. Each week, update the repository using the 'Sync fork' button in GitHub to check for changes, if it is out of date
   then select the 'Update branch' button.

## Activity instructions and code files

The `activities` folder contains the activity instructions for each week.

The `src-student` package contains any starter code for each week. You can also use this package to store your own code
that you create during the activities.

One solution to the week's activities will be added to the [tutor_solution directory](src/tutorialpkg/tutor_solution)
the following week. Other solutions will be possible, and some may be better than the solution offered, so don't feel
your code has to match the tutors code!

## List of activity instructions

This will be updated each week with the activities for that week.

### Week 1 Setting up a project in your IDE (VS Code, PyCharm) using source code control and python virtual environment
[Week 1 instructions](activities/week1/1-0-instructions.md)
1. [Create a repository directly on GitHub (10 mins)](activities/week1/1-1-create-repository-github.md)
2. [Create a repository using GitHub Classroom (10 mins)](activities/week1/1-2-create-repository-github-classroom.md)
3. [Create a repository by forking a GitHub repository (5 mins)](activities/week1/1-3-create-repository-fork.md)
4. [Find a repository (5 mins)](activities/week1/1-4-find-repository.md)
5. [Integrate your IDE with your GitHub account (10 mins)](activities/week1/1-5-integrate-IDE-github.md)
6. [Clone a repository to create a project in your IDE (5 mins)](activities/week1/1-6-clone-repository.md)
7. [Create a virtual Python environment for a project in your IDE (10 mins)](activities/week1/1-7-create-virtual-environment.md)
8. [Synchronise changes between the local and remote repository (5 mins)](activities/week1/1-8-synch-changes.md)

### Week 2 Data preparation using Python pandas
[Week 2 instructions](activities/week2/2-0-instructions.md)
1. [Create a package and module](activities/week2/2-01-python-structure)
2. [Open .csv and .xlsx files and create a DataFrame](activities/week2/2-02-pandas-open)
3. [Describe the dataframe](activities/week2/2-03-pandas-describe)
4. [Change data types](activities/week2/2-04-pandas-datatypes)
5. [Combine dataframes](activities/week2/2-05-pandas-joining-dataframes)
6. [Remove columns](activities/week2/2-06-pandas-removing-columns)
7. [Deal with missing values](activities/week2/2-07-pandas-missing-values)
8. [Columns with categorical values](activities/week2/2-08-pandas-categorical-data)
9. [Add new column](activities/week2/2-09-pandas-new-column)
10. [Save prepared data to .csv](activities/week2/2-10-save-df-to-file.md)
11. [Suggestions for further practice](activities/week2/2-11-further-practice)

### Week 3 Data preparation and visualisation using Python pandas and matplotlib
[Week 3 instructions](activities/week3/3-0-instructions.md)
1. [Introduction to pandas plotting](activities/week3/3-1-plot-overview)
2. [Plotting distributions using histograms](activities/week3/3-2-distribution)
3. [Identifying outliers using boxplots](activities/week3/3-3-outliers.md)
4. [Plotting timeseries](activities/week3/3-4-timeseries.md)
5. [Chart styling](activities/week3/3-5-chart-styling.md)
6. [Check your code complies with Python style guides](activities/week3/3-6-lint)
7. [Code AI](activities/week3/3-7-aitools.md)

### Week 4 Database design and creation using Python sqlite3
[Week 4 instructions](activities/week4/4-0-instructions.md)
1. [Introduction to database design and ERD (lecture recap)](activities/week4/4-1-database-design.md)
2. [Design and draw an Entity Relationship Diagram (ERD) for a database normalised to 3rd normal form (3NF)](activities/week4/4-2-ERD.md)
3. [Design and draw an Entity Relationship Diagram (ERD) for a database normalised to 3rd normal form (3NF) - part 2](activities/week4/4-3-ERD-part2.md)
4. [Data constraints and UPDATE/DELETE actions](activities/week4/4-4-constraints.md)
5. [Further practice/information](activities/week4/4-5-further-practice.md)

### Week 5 Database design and creation using Python sqlite3 continued
[Week 5 instructions](activities/week5/5-0-instructions.md)
1. [Introduction: Using Python sqlite3 and pandas to create SQLite databases](activities/week5/5-1-introduction.md)
2. [Create an un_normalised database from a pandas dataframe](activities/week5/5-2-create-studentdb-unnormalised.md)
3. [Create the structure for a normalised database using SQL, sqlite3 and pandas dataframe](activities/week5/5-3-studentdb-normalised-structure.md)
4. [Introduction to SQL SELECT for finding values from a table](activities/week5/5-4-select-query.md)
5. [Introduction to SQL INSERT for adding values to a table](activities/week5/5-5-insert-query.md)
6. [Add data to the normalised database](activities/week5/5-6-studentdb-normalised-add-data.md)
7. [Apply the knowledge to create the paralympics database](activities/week5/5-7-create-paralympics-db.md)

### Week 6 Requirements analysis, wireframes

[Week 6 setup](activities/week6/6-0-instructions.md)
1. [Introduction to requirements](activities/week6/6-1-introduction.md)
2. [Identifying requirements](activities/week6/6-2-identify-requirements.md)
3. [Documenting requirements](activities/week6/6-3-document-requirements.md)
4. [Prioritising requirements](activities/week6/6-4-prioritise-requirements.md)
5. [Wireframes](activities/week6/6-5-wireframes.md)

### Week 7 Application design
[Week 7 setup](activities/week7/7-0-instructions.md)
1. [Introduction to application design](activities/week7/7-1-introduction.md)
2. [Identifying classes](activities/week7/7-2-identify-classes.md)
3. [Application design diagram](activities/week7/7-3-draw-design.md)
4. [Review the design against design principles](activities/week7/7-4-review-design.md)
5. [Draw the application design for the paralympics prediction web app](activities/week7/7-5-design-medals.md)
6. [Using gen AI tools in application design](activities/week7/7-6-genAI.md)

### Week 8 Database design, database queries
[Week 8 setup](activities/week8/8-0-instructions.md)
1. [Update the database design diagram (ERD) based on requirements](activities/week8/8-1-update-erd.md)
2. [SQL SELECT queries](activities/week8/8-2-select.md)
3. [SQL SELECT queries with JOIN - where data is in two or more related tables](activities/week8/8-3-join.md)
4. [SQL INSERT queries](activities/week8/8-4-insert.md)
5. [SQL UPDATE queries](activities/week8/8-5-update.md)
6. [SQL DELETE queries](activities/week8/8-6-delete.md)
7. [Final ERD for the paralympics database](activities/week8/8-7-erd-paralympics-final.md)

### Week 9 Unit testing with pytest and continuous integration using GitHub Actions
[Week 9 setup](activities/week9/9-0-instructions.md)
1. [Introduction to testing](activities/week9/9-1-introduction.md)
2. [Unit testing](activities/week9/9-2-unit-testing.md)
3. [Fixtures](activities/week9/9-3-fixtures.md)
4. [GitHub Actions for continuous integration](activities/week9/9-4-ci-github.md)
5. [Coverage](activities/week9/9-5-coverage.md)
6. [Using gen AI in testing](activities/week9/9-6-ai-testing.md)
7. [Further information](activities/week9/9-7-further.md)

### Week 10 Coursework support

No new activities this week. This is the final week of the module, please use the session to complete the coursework.
The course tutor and PGTAs will be in the usual tutorial rooms to answer any questions.
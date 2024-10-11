# Introduction to using generative AI within COMP0034 and COMP0035

The information in this activity is adapted from UCL sources; the introduction is largely reproduced from the UCL "AI
and
You" teaching toolkit.

## Introduction

Large language models such as ChatGPT can generate text in multiple languages and styles. They can also interpret text
and images.

ChatGPT has an increasing list of plugins that extend the natural language model to connect to services, data, and
calculations.

Consider the limitations:

- LLMs are highly trained text-predictors. Their responses are based on probable language. Factual information may
  therefore contain inaccuracies that sound plausible but are often entirely incorrect. For example, LLMs may invent
  quotes, references, or coding libraries.
- LLMs only have access to the data they were trained on and therefore don’t have access to current information.
- LLMs cannot perform complex computations and are not perfect at interpreting language. They simply predict the most
  likely sequence of words.

## The broader ethical issues

### Regulation

There is currently no regulation of generative AI. Its rapid development has caused apprehension for many leading
figures and calls to pause its development.

### Privacy and data

Generative AI is built on information scraped from the internet without permission and often in violation of
intellectual property rights. OpenAI has no data regulation policy and may collect sensitive information from users
through prompts.

### Cognitive bias

Generative AI has no ethical principles. It is a tool that collects information from databases and texts it processes on
the internet. Its predictions repeat the cognitive biases found in that information.

### Environment

Training LLMs produce significant carbon emissions. Researchers suggest that training ChatGPT-3, for example, generated
552 tons of carbon dioxide. Equivalent to 123 petrol cars driven for one year.

### Human rights

Generative AI requires invisible human labour to build and cleanse. OpenAI employed workers in Kenya in gruelling
conditions for less than $2 an hour.

## UCL rules on academic integrity and AI

UCL has developed three categories to provide guidance for when and how students can use generative AI in their
assessments. Each category describes a general approach with examples. You are free to adapt these categories, offer
additional clarification, and include different examples. The three categories are:

Category 1:    Students are not allowed to use generative AI for their assessment beyond what is specified in the UCL
Academic Manual (9.2.2b).

Category 2:    Students are permitted to use generative AI tools for specific purposes to assist with their assessment.

Category 3:    Generative AI is an integral part of the assessment and students are supported and encouraged to use it
extensively.

Departments and/or module leaders will need to decide which category to employ for their assessments in advance. This
should be communicated to students in a standardised manner. Assessment cover sheets could include a statement for
students to declare “I have read, understood and abided by the restrictions on the use of generative AI for this
assignment.”

## Use of generative AI in COMP0035

The assessments in COMP0035 fall into category 2. The descriptor for this category is
> "AI tools can be utilised to
> enhance and support the development of specific skills in specific ways, as specified by the tutor and required by the
> assessment. For instance, students might use AI for tasks such as data analysis, pattern recognition, or generating
> insights. Here the tutor should support and guide the students in the use of AI to ensure equity of experience, but
> the
> use of AI is not in itself a learning outcome. There will be some aspects of the assessment where the use of AI is
> inappropriate."

The ethical issues, or other concerns, may lead you to choose not to use generative AI in this module. The assessments
are intended such that use of gen AI is optional and not intended to give advantage to those using them, nor
disadvantage
to those not using them.

The approach taken in the course materials is to first teach you to develop the necessary skills; they offer suggestions
to how gen AI could be used, and then invite you to reflect on their use e.g. by comparing the output from your initial
work to a result that is AI generated.

Specific tools are mentioned and used in the teaching materials, yet this does not imply they are
recommended. [UCL suggests the use of copilot](https://liveuclac.sharepoint.com/sites/Office365/SitePages/Bing-Enterprise-Chat.aspx).
Copilot is also available in tools that integrate with VS Code and PyCharm, this is not the same as accessing the Bing
Enterprise Chat version.

Some of the potential uses for generative AI within the course:

- Further practice and examples beyond the tutorial activities
- Assistance with debugging
- Understanding code samples
- Comparing your code or design diagrams to an AI generated version

## UCL links for students

Familiarise yourself with the UCL guidance for students
on [Engaging with AI in Your Education](https://www.ucl.ac.uk/students/exams-and-assessments/assessment-success-guide/engaging-ai-your-education-and-assessment).

Review UCL guidance
on [how to acknowledge and reference AI](https://library-guides.ucl.ac.uk/referencing-plagiarism/acknowledging-AI).

[Generative AI and Academic Skills](https://moodle.ucl.ac.uk/course/view.php?id=34355), an introductory course on UCL
Moodle for students and staff

Explore UCL student perspectives on GenAI:

- Student focus groups: Chandler, J.
  2023, [Student Perspectives on Ethical Usage of AI at UCL](https://liveuclac-my.sharepoint.com/:b:/g/personal/ucrajoc_ucl_ac_uk/EYr1OkuiGtJEkCVaA7wWhFwBAKr5q4F0S75jm7HFmHLM4g?e=rYa1Xw).
- Short video interviews with students on [how they use AI tools](https://mediacentral.ucl.ac.uk/Play/98514)
  and [academic integrity and AI literacy](https://mediacentral.ucl.ac.uk/Play/98516%C2%A0) on MediaCentral

## AI links related to the coding tools

- [GitHub Copilot Fundamentals - Understand the AI pair programmer](https://learn.microsoft.com/en-gb/training/paths/copilot/)
- [PyCharm AI assistant](https://www.jetbrains.com/help/pycharm/ai-assistant.html)
- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)

## Activities related to week 3

For each activity:

1. Write/create your own version
2. Write a prompt to generate an AI version
3. Compare the gen AI output to your own and reflect

    - Would you adapt your work based on the AI result? If so how?
    - Have your learned anything from the comparison?
    - Has the gen-AI aided your understanding?
4. Consider repeating the same prompt with a different gen-AI tool and comparing the results.

Activities:

1. Write/improve code e.g. Prompt "Write Python code that is an example of how to use pandas to read a csv file into a
   DataFrame" and as a second prompt "Add error handling".
2. Add documentation e.g. you should have written at least one function in your code. Prompt: "Add a docstring to this
   following python function" and copy and paste the code into copilot.
3. Explain a concept e.g. "How does pandas.plot work?" or "Explain linting in Python".
4. Generate code from a docstring. e.g. prompt "Complete the Python code for this docstring" and paste this example:

    ```python
    class BankAccount:
        """
            A class used to represent a Bank Account.
        
            Attributes:
            ----------
            account_holder : str
                the name of the account holder
            balance : float
                the current balance of the account
        
            Methods:
            -------
            deposit(amount):
                Adds the specified amount to the account balance.
            withdraw(amount):
                Deducts the specified amount from the account balance if sufficient funds are available.
            get_balance():
                Returns the current balance of the account.
            """
    ```
5. Using the code genAI tools in VS Code or PyCharm

    - [CoPilot with Jetbrains PyCharm](https://docs.github.com/en/copilot/getting-started-with-github-copilot?tool=jetbrains#about-github-copilot-and-jetbrains-ides)
      Follow the instructions in the link to download the plugin and login to GitHub using the PyCharm | Tools | GitHub
      Copilot login option. It will require you to copy and enter a code.
    - Open `ai-docstring.py`
    - Line 1 before the docstring, start typing 'def ' and it should prompt you by offering a meaningful function name.
    - Place the cursor by the start of the docstring, and again it should offer you code to complete the functon; you
      may need to select the Refresh option in the GitHub copilot window.
    - Accept the code, and you should have a function with a docstring.

    - [CoPilot with VS Code](https://docs.github.com/en/copilot/getting-started-with-github-copilot?tool=vscode#prerequisites-2).
      Use the reference to set up VS Code to work with GitHub CoPilot.
    - Open `ai-docstring.py`.
    - On line 1 start typing 'def ' and it should prompt you by offering a meaningful function name.
    - Hover over the start of solution - it should correct the indentation and provide an implementation of the code.
    - This is only a simple example. In VS Code the CoPilot feature functions with the lightbulb to offer
      auto-completion of code and adding documentation to code.

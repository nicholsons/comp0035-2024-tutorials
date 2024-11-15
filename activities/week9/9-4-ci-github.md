# Running tests in GitHub Actions

The practice of automatically running tests as part of the development cycle is a practice referred to as Continuous
Integration (refer to lecture notes).

GitHub provides a way to configure and run tests on a given action such as when a new commit is made to your repository.
The tool used for this is GitHub Actions.

How to use GitHub Actions is more
fully [documented on GitHub's site](https://docs.github.com/en/actions/writing-workflows).

GitHub Actions can be created in a number of ways. In this activity you will use a workflow template provided on GitHub
and edit it to your needs.

## Create a GitHub Actions workflow

You can practice on your tutorials repository and then apply it to your coursework repository.

Steps:

- Go to your repository on GitHub
- Go to the **Actions** tab
- Find the workflow named **'Python application'** and click on **'Configure'**
    - You will see a workflow `.yml` file generated on the screen. Edit this with the following changes:

        - In the section `name: Install dependencies` at the end of this section but before the `name: Lint with Flake
          8` add a line to install your code `pip install -e .`
          ```yaml
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install flake8 pytest
              if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
              pip install -e .
          ```
        - Find the **'commit changes...'** button which is likely to top right of the screen and press it. Change the
          message if you wish and then **'Commit changes'** again.

This workflow will now run every time you push a change to GitHub. This is useful as it runs all your tests so you can
see if new code you have written breaks any previously working functionality.

By default, GitHub Actions sends an email when the flow fails. You
can [change the notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#)
in GitHub.

## View the workflow results

To view the results of the workflow:

1. Go to the Action tab in your GitHub repository.
2. There should now be at least one workflow run. If all went well it has a green tick, if there were issues there will
   be a red cross. If there is a Amber/Yellow circle then the workflow is still running.
3. Click on the tick/cross/circle on the workflow.
4. Click on the tick/cross/circle on 'build'.
5. You should now see headings that correspond to the `name: ` sections in the .yml file.
6. Expand the `Test with pytest` section. The output should look similar to what you saw when you ran pytest from the
   terminal.

If there is a red cross then find the section at step 5 that has the red cross, expand it and see what the error message
it. It should say what failed and why. You will then need to fix the error.

Note: if the tests fail with a 'module not found' error this is likely due to either not adding the line
`pip install -e .` in the installation section of the .yml, or an issue with the content of pyproject.toml.

[Next activity](9-5-coverage.md)
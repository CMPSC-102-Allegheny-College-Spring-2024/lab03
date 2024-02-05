# Working in Virtual Environments

## Assigned: Monday, 5 February 2024

## Due: Monday 12 February 2024

## Expiration date: 19 February 2024

## Project Goals

To gain experience in using virtual environments.
To transform a piece of code to work in the Poetry virtual environment where command-line-parameters are employed to use the code.

## Objective

In class, we have been talking about using virtual environments for the development of projects in computer science. Often developers will have several projects going at the same time where each project requires the same library but, perhaps, a different version of the library. With a virtual environment, all associated resources remain tied to specific projects, and do not haphazardly become inter-twined with other projects by accident.

In this lab, you will gain experience in programming with Poetry to complete a Python project to allow CLI inputs (i.e., parameters) to initiate the code. The function of the program is to collect and record simple data from the user which is saved in the File `user_data.csv`. The collection of information is to be completed __only__ by CLI parameters which are then formatted b the code to create the data file. The data itself is comprised of information regarding the user's _name_, in addition to their favorite _film_, _song_ and _food_.

Your task is to complete the provided code in the directory `to function with Poetry so that users may enter build the data file from executing the poetry project from the command line. Remember to use your notes from class to assist you in completing the work.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in a course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!


## Executing the code

In order to run this project, you must first go to the directory, `csvFiler/` where you will be able to see the File, `pyprojject.toml`. If you cannot locate this file in your current directory, then you are not in the correct working directory and the following commands will not execute correctly.

+ Type the following command to build the File `poetry.lock` after loading all necessary libraries for the project.

``` bash
poetry install 
```

+ To execute the code, use the following command.

``` bash
poetry run csvfiler --name myname --ghhandle myHandle --favfilm myfilm --favsong mysong --favfood myFood
```

## Expected Output

With completed code, and after the command-line parameters have been entered, your output will appear as the following.

``` bash
✨ Your name: myname
✨ Your GitHub name: myHandle
✨ Your favorite film: myfilm
✨ Your favorite song: mysong
✨ Your favorite food: myFood
```

+ The code is shown below to create this output is found in the `main()` function.

``` python linenums="1"
    console.print(f":sparkles: Your name: {name}")
    console.print(f":sparkles: Your GitHub name: {ghhandle}")
    console.print(f":sparkles: Your favorite film: {favfilm}")
    console.print(f":sparkles: Your favorite song: {favsong}")
    console.print(f":sparkles: Your favorite food: {favfood}")
```

## Data File

The file `user_data.csv` will be created in the local directory containing the inputted data on a single line. If the file previously existed, then the file is conveniently appended with a line of the new data.

## Special Note

The file `pyproject.toml` is a configuration file in which you are connect the command lines to the function that actually does the work. In this project, this configuration file has already been completed for you, however, it is important to understand what parts of the code make this connection. In the configuration code below, we note that the Program `csvfiler` is driven by the File `main.py` which accepts the command-line-inputs from the user.  When you create a project in _Poetry_, you will have to add similar code to direct user-inputs to a driver function of the code.

``` bash
[tool.poetry.scripts]
csvfiler = "csvfiler.main:cli"
```

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and used, and answer all of the other questions about your experiences in completing this project. For instance, your technical writing in the `writing/reflection.md` file should make it clear that you understand the concept of an "imaginary" number and the notation that the Python programming language uses to express these numbers.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ``` bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

+ **GitHub Actions CI Build Status [up to 50%]:**: For the lab02 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

+ **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

+ **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

* Extra resources for using markdown include;
  + [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Do not forget to use the above git commands to push your work to the cloud for the instructor to grade your assignment. You can go to your GitHub repository using your browser to verify that your files have been submitted. Please see the TL’s or the instructor if you have any questions about assignment submission.

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.

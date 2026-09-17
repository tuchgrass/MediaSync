Collaborative Software Development with Git & GitHub
Industry
general
Tools
bash
github
Skills
code-versioning
git-version-control
Overview
In this hands-on exercise, you are part of TechNova Solutions, a fast-growing AI startup building MediSync, an AI-powered healthcare management system. Given the distributed nature of the development team, effective version control is essential to ensure smooth collaboration, prevent conflicts, and maintain a clean project history.

Through practical exercises, you will learn how to use Git and GitHub to track changes, manage branches, and collaborate effectively. By the end of this hands-on, you will have experience in creating repositories, making commits, working with branches, merging changes, and pushing code to GitHub—all fundamental skills for any developer working in a team environment.

1
You are a part of TechNova Solutions, a fast-growing startup specializing in AI-powered healthcare applications. The company is building a new product called MediSync, which helps hospitals and clinics manage patient records seamlessly.

The development team is distributed across different locations, and collaboration is key. Since multiple developers are working on the same codebase, version control using Git & GitHub is essential to ensure smooth collaboration and avoid overwriting each other’s work.

2
Why is version control important in the development of MediSync?

To ensure only one developer can work on the code at a time

To track changes, collaborate effectively, and prevent overwriting work

To track changes, collaborate effectively, and prevent overwriting work

To store project files on a local machine without backup

To store project files on a local machine without backup

To avoid using Python for development

To avoid using Python for development

3
Task 1: Setting Up the GitHub Repository and Making the First Commit

You have been assigned to work on MediSync, an AI-powered healthcare management system. Since this is a collaborative project involving multiple developers, using Git and GitHub for version control is crucial.

Your team needs a central repository to store the project files, track changes, and collaborate effectively. To get started, you will create a repository on GitHub, clone it to your local machine, and add some initial project files.

Step 1: Create a GitHub Repository
To begin, you need to create a remote repository on GitHub.

Name the repository MediSync (or any suitable name).
Keep the repository public so your team can access it.
Do not initialize it with a README, .gitignore, or license (you will add these manually).
Step 2: Clone the Repository to Your Local Machine
Now that the repository is set up, you need to bring it to your local system. Clone the repository using its HTTP URL so that you can start working on the project files.

Step 3: Add Initial Project Files
Once you have the repository on your local machine, navigate inside the cloned folder and create the following files:

Main Python script (app.py) – This will contain the core logic for AI-powered patient management.
A text file (notes.txt) – This file will be used for rough ideas, personal notes, or scratchpad content.
A .gitignore file – This special file tells Git which files or file types to ignore during staging and committing.
For now, the file will be empty, but later, we will add rules to exclude certain files (e.g., .txt, .csv, temporary files, etc.).
Step 4: Add Code to app.py
Now, open the app.py file and add the following Python code to simulate a basic patient management system:

# app.py - Core logic for AI-powered patient management

class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition

    def display_info(self):
        return f"Patient: {self.name}, Age: {self.age}, Condition: {self.condition}"

# Sample usage
if __name__ == "__main__":
    patient1 = Patient("John Doe", 45, "Diabetes")
    print(patient1.display_info())
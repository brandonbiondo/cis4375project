# Contribution Guide for Feature and Fix Branches
This guide outlines the recommended workflow for contributing new features or fixing issues to a repository hosted on GitHub, using Git and feature/fix branches.

### Setting Up Your Environment
Before you can contribute to a repository on GitHub, you need to set up your development environment. Follow these steps to get started:

1. Install Git on your local machine.
2. Clone the repository you want to contribute to using `git clone [repository url]`.  
3. Create a new branch for your feature or fix using `git checkout -b [follow the guide below]`. Example: `git checkout -b brandonbiondo/feature-login-page`
    - Naming your branch (Make sure to follow this format): `<username>/<feature>-name-of-feature`.
    - Naming your branch (Make sure to follow this format): `<username>/<bug>-name-of-bug`.
    - Naming your branch (Make sure to follow this format): `<username>/<comment>-name-of-comment`.

### Working on Your Branch
Once you've set up your environment and created a new branch, you can start working on your changes. Here are some best practices to follow when working on your branch:

* Keep your commits small and focused on a single task.
* Write descriptive commit messages that explain what changes you made.
* Test your changes thoroughly before submitting a pull request.
* Rebase your branch on the latest version of the main branch to ensure that your changes are up to date.

### Pushing Changes to GitHub
When you're ready to submit your changes, you can push your branch to GitHub and open a pull request. Here's how to do it:

1. Push your branch to GitHub using git push -u origin [branch-name].
2. Go to the repository on GitHub and click the "Compare & pull request" button.
3. Write a detailed description of your changes in the pull request.
4. Wait for feedback from other contributors or the repository maintainer.

### Reviewing Pull Requests
If you're a repository maintainer or another contributor, you may be asked to review a pull request. Here are some best practices to follow when reviewing a pull request:

* Review the changes thoroughly and test them if possible.
* Provide constructive feedback in a polite and respectful manner.
* Approve or reject the pull request based on whether it meets the repository's contribution guidelines.

### Merging Pull Requests
Once a pull request has been approved and all feedback has been addressed, it can be merged into the main branch. Here's how to do it:

1. Click the "Merge pull request" button on the pull request page.
2. Write a detailed commit message that summarizes the changes in the pull request.
3. Click the "Confirm merge" button to merge the pull request.

### Conclusion
By following these guidelines, you can contribute new features and fixes to a repository hosted on GitHub in a way that is efficient, effective, and respectful to other contributors. Happy contributing!

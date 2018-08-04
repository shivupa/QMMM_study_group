# Contributing

This project welcomes contributions in the form of example notebooks, example code, theory documentation, and bug fixes. Below there are directions on how to get started as well as guidelines on contributions.


# Getting started
## 1. Fork this repository
This creates a copy for you on your Github page (Click the button that says fork this repository). The changes you make to this version will not be a part of everyone's code yet.

## 2. Clone your fork locally
This creates a local copy on your computer(s) that you can edit. 

## 3. Add remote
Once your forked copy of the repository is cloned locally, you will want to add the main repository as an upstream source in order to get any changes that are made to the main repository. To do this, add the main repository as an upstream source by `git remote add upstream https://github.com/shivupa/QMMM_study_group`. Check that the upstream was added by running `git remote -v`. If added correctly, you should be able to `git pull upstream master` in order to obtain any new changes made to the main repository.

## 4. Create development environment
To ensure that all of us are working with the same packages and libraries, we have provided a `environment.yml` file in the root directory of this repository. This helps to reduce the number of "well, it works on my system" allowing for all users to be able to setup the environment and immediately try out the notebooks. Instructions for how to set up the provided development environment can be found in the [wiki](https://github.com/shivupa/QMMM_study_group/wiki/Environment-Setup).

## 5. Add notebooks, code, presentations, or fix bugs

## 6. Add the changes to your forked version
To see what files have changed use the command `git status`.
Add the files that you have changed using `git add filename`.
Explain what changes you have made using an informative commit message with `git commit -m "My message.."`.
Push the changes to your forked version using `git push`.

[Git](https://git-scm.com/docs/gittutorial) provides great tutorials on how to use git for version control for your projects.

## 7. Add your changes to the main repository
Go to the [main repository](https://github.com/shivupa/QMMM_study_group) and open a pull request from *your* master branch to the project master branch. For more information on pull requests see [GitHub Help: About pull requests](https://help.github.com/articles/about-pull-requests/). Also, **DO NOT** merge your own pull requests.

# Guidelines
Not following these guidelines will ensure your pull request is not merged.

## Directory structure
For best readability and consistency each topic will contain be a topic directory. In this topic directory there needs to be the pdf presentation of the topic (if applicable), a basics directory, and an advanced directory. The basics directory will contain framework notebooks/code that supplements the presentation of that topic. After a few days a solution notebook needs to be added to the basics directory. The advanced directory will contain notebooks/code that further builds on the topic such as faster algorithms or accounting for more complex systems. 


## Naming 
#### Topic directory
Topic directories are named such that the first letter in the name of the directory and all letters in the techniques name are capitalized.  
Example: 05_Modern_DFT

#### Subdirectories and files
All subdirectories and files need to be lowercase. Do not use spaces in names, use underscores.  
Example: uhf_psi4.ipynb 

## Presentation
The topic presentation can be made in your preferred presentation editor but must be exported as a pdf.

## pep8
This project aims to follow the [pep8 style guide](https://www.python.org/dev/peps/pep-0008/) for python programming. The development environment that we provide includes a package, jupyter notebook extensions, that allows users to use the package autopep8 to help ensure the notebooks follow the pep8 style guide. This extension is off by default but can be turned on in the Nbextension tab after launching jupyter notebook by clicking the box next to autopep8. To autopep8 a jupyter notebook, hold down shift and select the hammer icon.


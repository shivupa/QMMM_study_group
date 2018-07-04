# QMMM_study_group
QM/MM Study Group

Meetings are Fridays at 10 am.


## Environment Setup
### 0. Clone QMMM_study_group

### 1. Download anaconda

For installation please download Python 3.6  from [Anaconda](https://www.anaconda.com/download/). From there follow the directions below to install Anaconda for your specific operating system.

- #### Linux or Windows Subsystem for Linux (WSL)
 - Open terminal and cd to directory where you downloaded the file to.
 - ```bash Anaconda-latest-Linux-X86_64.sh```

- #### macOS
 - Download ```.pkg``` from [Anaconda](https://www.anaconda.com/download/#macos).
 - Double click on the ```.pkg``` and follow directions.

- #### Windows
 - Download ```.exe``` from [Anaconda](https://www.anaconda.com/download/#windows).
 - Double click on the ```.exe``` and follow directions.

### 2. Create QM/MM Environment
- #### Linux, macos, WSL
 - Open terminal and cd into QMMM_study_group
 - ```conda env create -f environment.yml```

- #### Windows (Dakota is not sure if this is correct please let him know if it is or not)
 - Open command prompt and cd into QMMM_study_group
 - ```conda env create -f environment.yml```

### 3. Test environment
Open terminal and tryout below

```
user@computer ~ $ source activate qmmm
(qmmm) user@computer ~ $ python -V
Python 3.6.6 :: Anaconda, Inc.
(qmmm) user@computer ~ $ python
Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 11:07:29)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> 4 * np.pi
12.566370614359172
>>> quit()
(qmmm) user@computer ~ $ source deactivate
user@computer ~ $
```
Note: The initial output from the Python shell will look different for your system

If there are any issues setting up this environment, please contact us by email, notify us on Slack, or create an issue.

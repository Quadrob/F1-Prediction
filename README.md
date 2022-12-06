# F1-Predict
![Concept Car](/Assests/readme.webp.png)

## Table Of Contents
-   [Overview](#overview)
-   [QuickStart](#quickstart)
-   [Compatibility](#compatibility)
-   [Installation Instructions](#installation-instructions)
-   [Startup Instructions](#startup-instructions)
-   [Tools Used](#tools-used)
-   [Machine Models Used](#machine-models-used)
-   [Next Steps](#next-steps)
-   [Feedback](#feedback)
-   [Credits](#credits)
-   [Additional Resources](#additional-resources)
---

## Overview
For this school project, I proposed creating a machine learning application that would designed to predict outcomes in a sporting spectacle. I decided to focus the project on motor vehicle racing, more specifically Formal 1, which is the pinnacle of motorsports and is commonly referred to as F1. This F1 prediction application is able to predict qualifiction, race, and championship results for both a driver as well as a constructor. In addition, it pridicts the best constructor for a driver or the best two drivers for a constructor. It leverages data analytics to predict future results, taking into consideration the driver performance metrics, constructor (team) performance metrics, and external factors that impact the resulting outcome. 

---

## QuickStart
### Open Official F1-Predict Documentation
*   Click on `Open-F1-Predict-Documentation.bat` in the root directory of the project to open the official docs.

### Start F1-Predict Application
*   Click on `Start-F1-Predict.bat` in the root directory of the project to open the F1-Predict application.

---

## Compatibility
### Recommended:
#### Hardware
>      1.6 GHz or faster processor
>      1 GB of RAM
>      Hard disk space: Minimum of 200 MB
#### Operating System
>      OS X El Capitan (10.11+)
>      Windows 8.0, 8.1 and 10, 11 (32-bit and 64-bit)
>      Linux (Debian): Ubuntu Desktop 16.04, Debian 9
>      Linux (Red Hat): Red Hat Enterprise Linux 7, CentOS 7, Fedora 34
#### Supported Languages
>      English
#### Additional Requirements
>      Administrator rights are required to install or update

---

## Installation Instructions
### Steps to Install Git
1.  To use this project you will need to use Git to clone the repository. Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package, via installer, or download the source code and compile it yourself. Navigate to the [getting started with Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) page and scroll to the section relating to your operating system to begin. 
2.  Open [F1-Predict Repository](https://github.com/Quadrob/F1-Prediction) and click the green code drop-down button on the top left. From the drop down copy the `https` link which will use in a later step. The link should look like:
```cmd
    https://github.com/Quadrob/F1-Prediction.git
```
3.  Once you have Git installed on your machine, create a folder where you would like the project to be checkedout to and open a Git bash terminal (`right-click` and `Git Bash Here`). Type in the bash terminal `git clone <repo-url>` for example: <br/>
```cmd
    git clone https://github.com/Quadrob/F1-Prediction.git
```
4.  Once this command completes it will have cloned the F1 Predict repository to your local machine.

---

### Install Python
1.  This project was developed in the [Python programming language](https://www.python.org/) that is easier to pick up and has some powerful features that assist with various topics such as image modification, Machine Learning, and Artificial intelligence (AI). To install Python on your local machine navigate to [Python Installer](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) which will start the download for you. 
>***IMPORTANT: Please make sure you download python version 3.7 or lower. Any version higher than 3.7 is incompatible with the tkinter library***
2.  Once the installer has downloaded you can open it, select the custom installation option, check the boxs next to the tools you would like to include, **ensure you install pip** and click next, **ensure you select 'add python to enviroment variables'**, then select where you would like to install python and finally click install.
>***IMPORTANT: Please make sure you add Python to your system PATH enviroment variable.*** To add Python to your enviroment variables please look at this guide: [Add Pthon To Enviroment Variables](https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows).
3.  You can varify that the installation was successful by opening up a command line terminal and executing the `py -3.7` command as below:
```cmd
    C:\Users\rober> py -3.7
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    >>> exit()
```

---

### Pip Install Required Packages
1.  As a general-purpose programming language, Python is designed to be used in many ways with many powerful packages that add even more functionality. Python has a standard package manager, called `pip`, which allows you to install and manage packages that aren’t part of the Python standard library. It should have been installed with your python installation in the previous step.
2.  To install all the required packages necessary for running this project you can open up a command line terminal in the root folder of where you cloned the project and execute the following command:
```cmd
    py -3.7 -m pip install -r requirements.txt
```
>***IMPORTANT: If the pip install command fails then try reopening the command lind terminal as administrator.***

---

## Startup Instructions
I have detailed two ways of running the application below. If the instalation instructions were successfully completed, then by performing one of the below tasks will result in the applications splashscreen appearing and the project will execute.

### Run using a Batch File
*   The first and preffered option is to run the project by simply opening the `Start-F1-Predict.bat` file located in the root of the application.

### Run using the Command Line Terminal
*   The second option is to open up a command line terminal in the root directory of the project and execute the following command:
```cmd
    py -3.7 F1Predict.py
```

---

## Tools Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) ![replit](https://img.shields.io/badge/replit-667881?style=for-the-badge&logo=replit&logoColor=white) ![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=whit) ![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
```
VSCode
Git
Python 
SQLite
Numpy 
Pandas 
sklearn 
beautifulsoup4 
customtkinter 
Flask 
matplotlib 
Pillow 
python_dateutil 
requests 
selenium 
webdriver_manager 
```

## Machine Models Used
```python
Logistic Regression
XGBoost
```

---

## Next Steps
During this project I have been noting down things I believe could be done better as well as the feedback I have recived from friends and family who have helped test the application for me. This section details all of these notes and future hopes for the project.
```python
# Improvements to data collection:
# =========================================
# Get driver total points for data analysis and prediction
# Get constructor total points for data analysis and prediction
# Get driver total wins and podiums and poles for data analysis and prediction
# Get constructor total wins and podiums and poles for data analysis and prediction
# Implement caching of both results and database queries
# Get tire compounds for data analysis and prediction
# Get free practice results for data analysis and prediction
# Make data collection run automatically so the database is always up to date (perhaps in a background thread)

# Improvements to frontend:
# =========================================
# Improve UI for prediction pages ie: Style the results better or display in a table format
# Add another prediction option to display the results for all drivers / constructors not just one
# Change menu structure to improve application navigation
# Standardize UI styling ie: Round corner for buttons globally
# Improve the amount of wasted space on the application
# Improve the clearing of selected options so the users can reuse options for predictions
# Add more options the user can set to perform the prediction ie: tires, wind, practice 
# Allow the user to adjust the screen size to their prefrence
# The picture quality of some images needs to be improved
# Display drivers full name
# Display constructors full name
# Make season dropdown a number box with a max and min instead
# Make driver dropdown searchable
# Make constructor dropdown searchable

# Improvements to backend:
# =========================================
# Fine tune xgboost with data to improve results
# Divide the source code into smaller files ie: each class should be in its own file
# Use a single session Database connection 
# Implement more processes within its own thread to improve speed
# Make predictions with drivers from the specific season and not just current drivers
# Not every option needs a value to perform the prediction (exclude empty options from prediction)

# Improvements to other aspects:
# =========================================
# Build an .exe application of the project for easier installation, setup, and execution of the application
# Modify the project to allow it to run on replit editor online
# Make the project compatible with higher python versions
# Make wording consistent ie: use 'constructor' everywhere and not 'team' in some places and 'circuit' instead of 'track'
# Allow selection of any driver that has participated in an F1 race
# Allow selection of any constructor that has participated in an F1 race
# Menu option to browse the dataset or a simplified version of the database
# Improve Naming of the Pairing implemention
```

---

## Feedback
![ask me](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg) 
-   My Email Address:       **robertbots@gmail.com** 
-   My GitHub Account:      **https://github.com/Quadrob** 
-   My LinkedIn Account:    **https://www.linkedin.com/in/robert-zeelie/**

---

## Credits
>**Author:**    Robert Zeelie
>
>**Version:**   0.0.1
>
>![User Stats](https://github-readme-stats.vercel.app/api?username=Quadrob)

---

## Additional Resources
-   **I used [Ergast API](https://ergast.com/mrd/) as my Dataset for this project.**
-   **I used [XGBoost](https://xgboost.readthedocs.io/en/stable/index.html) my Machine Learning Model.**
-   **I used [TKinter](https://docs.python.org/3/library/tkinter.html) for my User Interface.**
-   **I used [Python Style Guide](https://google.github.io/styleguide/pyguide.html) for python styling guidence.**
-   **I used [pipreqs](https://pypi.org/project/pipreqs/) package to generate my requirmts.txt**

---

![F1 Logo](/Assests/F1-logo.png)
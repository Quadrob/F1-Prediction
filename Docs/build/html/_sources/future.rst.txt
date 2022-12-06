.. _future:

Future Improvments
==================
During this project I have been noting down things I believe could be done better as well as the feedback I have recived from friends and family who have helped test the application for me. This section details all of these notes and future hopes for the project.

Improvements to data collection
-------------------------------
*   Get driver total points for data analysis and prediction
*   Get constructor total points for data analysis and prediction
*   Get driver total wins and podiums and poles for data analysis and prediction
*   Get constructor total wins and podiums and poles for data analysis and prediction
*   Implement caching of both results and database queries
*   Get tire compounds for data analysis and prediction
*   Get free practice results for data analysis and prediction
*   Make data collection run automatically so the database is always up to date (perhaps in a background thread)

Improvements to frontend
------------------------
*   Improve UI for prediction pages ie: Style the results better or display in a table format
*   Add another prediction option to display the results for all drivers / constructors not just one
*   Change menu structure to improve application navigation
*   Standardize UI styling ie: Round corner for buttons globally
*   Improve the amount of wasted space on the application
*   Improve the clearing of selected options so the users can reuse options for predictions
*   Add more options the user can set to perform the prediction ie: tires, wind, practice 
*   Allow the user to adjust the screen size to their prefrence
*   The picture quality of some images needs to be improved
*   Display drivers full name
*   Display constructors full name
*   Make season dropdown a number box with a max and min instead
*   Make driver dropdown searchable
*   Make constructor dropdown searchable

Improvements to backend
-----------------------
*   Fine tune xgboost with data to improve results
*   Divide the source code into smaller files ie: each class should be in its own file
*   Use a single session Database connection 
*   Implement more processes within its own thread to improve speed
*   Make predictions with drivers from the specific season and not just current drivers
*   Not every option needs a value to perform the prediction (exclude empty options from prediction)

Improvements to other aspects
-----------------------------
*   Build an .exe application of the project for easier installation, setup, and execution of the application
*   Modify the project to allow it to run on replit editor online
*   Make the project compatible with higher python versions
*   Make wording consistent ie: use 'constructor' everywhere and not 'team' in some places and 'circuit' instead of 'track'
*   Allow selection of any driver that has participated in an F1 race
*   Allow selection of any constructor that has participated in an F1 race
*   Menu option to browse the dataset or a simplified version of the database
*   Improve Naming of the Pairing implemention
*   Improve Documentation Images



.. _testing:

Testing Documentation
=====================
User Testing
------------
For user testing I shared the F1 Predict repository with several friends and family. I asked then them to follow this documentation to install and conficure the application. Once they had setup everything I asked then to run through the very basic test plan below. If the basic test plan was executed successsfully i asked then to just navigate around the application and try using the predictions.

User Feedback
-------------
Issues
~~~~~~~~
Most of my friends and family were able to setup the application however one of my friends had another version of python on his machine that was setup in his enviroment variables which confused pip as the libraries and packages were installed for that python resulting in missing packages when trying to run the application.

Changes
~~~~~~~~
A few of my friends and family had some feedback for me:

*   Allow selection of any driver that has participated in an F1 race
*   Make driver dropdown searchable
*   Make constructor dropdown searchable
*   Allow selection of any constructor that has participated in an F1 race
*   Make predictions with drivers from the specific season and not just current drivers
*   Improve UI for prediction pages ie: Style the results better or display in a table format
*   Add another prediction option to display the results for all drivers / constructors not just one
*   Menu option to browse the dataset or a simplified version of the database
*   Allow the user to adjust the screen size to their prefrence
*   The picture quality of some images needs to be improved

.. note:: I have added the user feedback to my future development list which can be viewed on the :ref:`future` page

Test Plan
---------

*   Start the application

    1.  You should see the splash screen popup
    2.  The open terminal should begin logging output oof the dataset
    3.  The main menu will be displayed

*   Navigate the application

    1.  Navigate to the `Predict Driver` menu
    2.  Navigate to the `predict Qualification` page
    3.  Navigate back to the `Predict Driver` menu
    4.  Navigate back to the `Main Menu`
    5.  Repeat for other pages

*   Data loading

    1.  Navigate to the `predict Qualification` page
    2.  Open driver dropdown and ensure the dropdown is populated
    3.  Open season dropdown and ensure the dropdown is populated
    4.  Open track dropdown and ensure the dropdown is populated
    5.  Open weather dropdown and ensure the dropdown is populated
    6.  Repeat for other pages

*   Prediction Display
    
    1.  Navigate to the `predict Qualification` page
    2.  Select a driver from the driver dropdown
    3.  Select a season from the season dropdown 
    4.  Select a circuit from the track dropdown
    5.  Select a weather condition from the weather dropdown
    6.  Click `Predict Result` and wait for it to finish loading
    7.  The selected options as well as a result should be displayed to the right
    8.  All dropdown options should be reset
    9.  Navigate away from the `predict Qualification` page 
    10. Navigate back to the `predict Qualification` page
    11. The results to the right should no loger be displayed


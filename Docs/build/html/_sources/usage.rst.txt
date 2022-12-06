.. _usage:

Usage
=====
In this section, you will find detailed documentation on how to use this application. The `Startup Instructions` section will explain how to run the application, the `Usage Instructions` section provides a concise guide to using the application, and the `Page Descriptions` section explains the purpose of each page in the application.

Startup Instructions
--------------------

.. note:: **IMPORTANT:** These Startup Instructions assume that you have completed the :ref:`installing` page successfully.

If the instalation instructions were successfully completed, then by performing one of the below tasks will result in the applications splashscreen appearing and the project will execute.

Run using a Batch File
~~~~~~~~~~~~~~~~~~~~~~
The first and prefered option is to run the project by simply opening the `Start-F1-Predict.bat <../../../Start-F1-Predict.bat>`_ file located in the root of the application.

Run using the Command Line Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The second option is to open up a command line terminal in the root directory of the project and execute the following command:

.. code:: python

    py -3.7 F1Predict.python

Usage Instructions
------------------
Main Menu
~~~~~~~~~

1.  Startup the F1 Predict application as instructed in the section above and you should see the splashscreen loading which indicates the application is loading all necessary application data into memory.
2.  Once the splashscreen disappears, the the main menu will be displayed and you will be presented with 4 buttons to choose from:

    -   **Predict Driver:** This button will take you to the F1 Predict Drivers Menu
    -   **Predict Constructor:** This button will take you to the F1 Predict Constructor Menu
    -   **Best Driver Team Pairing:** This button will take you to the F1 Driver & Team Pairing Menu
    -   **Quit:** This button will exit the application and remove all application data from memory

F1 Predict Drivers Menu
~~~~~~~~~~~~~~~~~~~~~~~~

3.  Once you navigate to this menu, you will be presented with 4 buttons to choose from:

    -   **Predict Qualification:** This button will take you to the F1 Predict Drivers Qualification page

        4.  Once you navigate to this page, you will be presented with 4 dropdown buttons and 2 normal buttons. To predict a drivers Qualification please select:

            -   A driver from the drivers dropdown
            -   A season from the season dropdown
            -   A Track from the track dropdown
            -   A weather condition from the weather dropdown
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultdriverQualifying.jpg
           :alt: example of Qualification results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Drivers Menu by clicking the `Drivers Menu` button at the bottom of the screen.

    -   **Predict Race:** This button will take you to the F1 Predict Drivers Race page
    
        4.  Once you navigate to this page, you will be presented with 4 dropdown buttons and 2 normal buttons. To predict a drivers Race please select:

            -   A driver from the drivers dropdown
            -   A season from the season dropdown
            -   A Track from the track dropdown
            -   A weather condition from the weather dropdown
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultdriverRace.jpg
           :alt: example of Race results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Drivers Menu by clicking the `Drivers Menu` button at the bottom of the screen.


    -   **Predict Driver Championship:** This button will take you to the F1 Predict Drivers Championship page
    
        4.  Once you navigate to this page, you will be presented with 2 dropdown buttons, 2 slider options, and 2 normal buttons. To predict a drivers championship please select:

            -   A driver from the drivers dropdown
            -   A season from the season dropdown
            -   A driver points slider to select the amount of points
            -   A driver wins slider to select the amount of wins
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultdriverChamp.jpg
           :alt: example of Championship results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Drivers Menu by clicking the `Drivers Menu` button at the bottom of the screen.


    -   **Main Menu:** This button will exit the F1 Predict Drivers Menu and navigate back to then Main Menu

F1 Predict Constructor Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.  Once you navigate to this menu, you will be presented with 4 buttons to choose from:

    -   **Predict Qualification:** This button will take you to the F1 Predict Constructor Qualification page

        4.  Once you navigate to this page, you will be presented with 4 dropdown buttons and 2 normal buttons. To predict a Constructor Qualification please select:

            -   A Constructor from the Constructor dropdown
            -   A season from the season dropdown
            -   A Track from the track dropdown
            -   A weather condition from the weather dropdown
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultconstructorQualifying.jpg
           :alt: example of Qualification results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Constructor Menu by clicking the `Constructor Menu` button at the bottom of the screen.

    -   **Predict Race:** This button will take you to the F1 Predict Constructor Race page
    
        4.  Once you navigate to this page, you will be presented with 4 dropdown buttons and 2 normal buttons. To predict a Constructor Race please select:

            -   A Constructor from the Constructor dropdown
            -   A season from the season dropdown
            -   A Track from the track dropdown
            -   A weather condition from the weather dropdown
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultconstructorRace.jpg
           :alt: example of Race results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Constructor Menu by clicking the `Constructor Menu` button at the bottom of the screen.


    -   **Predict Constructor Championship:** This button will take you to the F1 Predict Constructor Championship page
    
        4.  Once you navigate to this page, you will be presented with 2 dropdown buttons, 2 slider options, and 2 normal buttons. To predict a Constructor championship please select:

            -   A Constructor from the Constructor dropdown
            -   A season from the season dropdown
            -   A Constructor points slider to select the amount of points
            -   A Constructor wins slider to select the amount of wins
        
        5.  Once you selected a value for each variable you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/resultconstructorChamp.jpg
           :alt: example of Championship results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Predict Constructor Menu by clicking the `Constructor Menu` button at the bottom of the screen.


    -   **Main Menu:** This button will exit the F1 Predict Constructor Menu and navigate back to then Main Menu

F1 Driver & Team Pairing Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.  Once you navigate to this menu, you will be presented with 3 buttons to choose from:

    -   **Best Team for a Driver:** This button will take you to the F1 Predict Best Team For Drivers page

        4.  Once you navigate to this page, you will be presented with 1 dropdown button and 2 normal buttons. To predict the best team for a driver please select:

            -   A Driver from the Driver dropdown
        
        5.  Once you selected a driver you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/bestteamfordriver.jpg
           :alt: example of Best Team For Driver results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Driver & Team Pairing Menu by clicking the `Pairing Menu` button at the bottom of the screen.

    -   **Best Driver for a Team:** This button will take you to the F1 Predict Best Drivers For Constructor page
    
        4.  Once you navigate to this page, you will be presented with 1 dropdown button and 2 normal buttons. To predict the best 2 drivers for a team please select:

            -   A Constructor from the Constructor dropdown
        
        5.  Once you selected a constructor you can click on the `Predict Result` button at the bottom of the page wich will then display `Loading...` text on the right of the screen.
        6.  Once the application has finished loading and predicted the result it will display all the details to the right of the window.

        .. image:: /images/results/bestdriverforteam.jpg
           :alt: example of Best two Drivers For a Team results
           :align: center

        7.  Once you have finished analysing the predicted results you can return to the F1 Driver & Team Pairing Menu by clicking the `Pairing Menu` button at the bottom of the screen.
        
    -   **Main Menu:** This button will exit the F1 Driver & Team Pairing Menu and navigate back to then Main Menu


Page Descriptions
-----------------
SplashScreen Pages
~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/pages/splash.jpg
   :alt: example of SplashScreen
   :align: center
    
   *This is F1 Predict's Loading Screen on Startup. In the backgroung it starts a seperate thread that fetchs all necessary data from the database and loads it into memory for faster predictions.*

Manu Pages
~~~~~~~~~~

.. figure:: /images/pages/mainmenu.jpg
   :alt: example of Main Menu
   :align: center
    
   *This is the Main Menu of the F1 Predict application and from this page the user can navigate to any prediction menu or page.*


.. figure:: /images/pages/drivermenu.jpg
   :alt: example of Drivers Menu
   :align: center
    
   *This is the Driver Prediction Menu where a user can navigate to any of the below prediction pages:*

   -    Predict Qualification: This page allows a user to predict a drivers qualifying position as well as time behind the leader.
   -    Predict Race: This page allows a user to predict a drivers race finishing position using the predicted qualifying position as well.
   -    Predict Driver Championship: This page allows a user to predict a drivers world championship finishing position.


.. figure:: /images/pages/constructormenu.jpg
   :alt: example of Constructor Menu
   :align: center
    
   *This is the Constructor Prediction Menu where a user can navigate to any of the below prediction pages:*

   -    Predict Qualification: This page allows a user to predict a constructor qualifying position as well as time behind the leader.
   -    Predict Race: This page allows a user to predict a constructor race finishing position using the predicted qualifying position as well.
   -    Predict Constructor Championship: This page allows a user to predict a constructor world championship finishing position.


.. figure:: /images/pages/pairingmenu.jpg
   :alt: example of Pairing Menu
   :align: center
    
   *This is the F1 Driver & Team Pairing Menu where a user can navigate to any of the below prediction pages:*

   -    Best Team for a Driver: This page allows a user to predict the best constructor for the selected driver.
   -    Best Driver for a Team: This page allows a user to predict the best two drivers for the selected constructor.


Prediction Pages
~~~~~~~~~~~~~~~~

.. figure:: /images/pages/driverqualifying.jpg
   :alt: example of driver qualification prediction page
   :align: center
    
   *This is the prediction page for predicting the qualification position outcome of the selected driver.*
   
.. figure:: /images/pages/driverrace.jpg
   :alt: example of driver race prediction page
   :align: center
    
   *This is the prediction page for predicting the race finishing position of the selected driver.*

.. figure:: /images/pages/driverchamp.jpg
   :alt: example of driver championship prediction page
   :align: center
    
   *This is the prediction page for predicting the driver championship finishing position of the selected driver.*

.. figure:: /images/pages/constructorqualifying.jpg
   :alt: example of constructor qualification prediction page
   :align: center
    
   *This is the prediction page for predicting the qualification position outcome of the selected constructor.*
   
.. figure:: /images/pages/constructorrace.jpg
   :alt: example of constructor race prediction page
   :align: center
    
   *This is the prediction page for predicting the race finishing position of the selected constructor.*

.. figure:: /images/pages/constructorchamp.jpg
   :alt: example of constructor championship prediction page
   :align: center
    
   *This is the prediction page for predicting the constructor championship finishing position of the selected constructor.*

.. figure:: /images/pages/bestteamfordriver.jpg
   :alt: example of Best Team for a Driver prediction page
   :align: center
    
   *This is the prediction page for predicting the best constructor (team) for the selected driver.*

.. figure:: /images/pages/bestdriverforteam.jpg
   :alt: example of Best Driver for a Team prediction page
   :align: center
    
   *This is the prediction page for predicting the best two drivers for the selected constructor (team).*


User Roles
----------
Currently the application does not support user roles and management.
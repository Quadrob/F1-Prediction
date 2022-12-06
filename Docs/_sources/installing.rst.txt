.. _installing:

Installing
==========
Compatibility
-------------
Hardware

.. code:: 

    1.6 GHz or faster processor
    1 GB of RAM or larger
    Hard disk space: 200 MB or larger
    Any standard video card (GPU)

Operating System

.. code:: 

    Windows 8.0, 8.1, 10, 11 (32-bit + 64-bit)

Supported Languages

.. code::

    English

Additional Requirements

.. code:: 

    Administrator rights are required to install or update


Installation Instructions
-------------------------
Windows 8.0 (32-bit + 64-bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   Steps to Install Git

        1.  To use this project you will need to use Git to clone the repository. Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package, via installer, or download the source code and compile it yourself. Navigate to the `Download Git <https://git-scm.com/download/win>`_ page and download the windows setup for your operating system to begin. 

        .. image:: /images/gitDownload.jpg

        2.  Open `F1-Predict Repository <https://github.com/Quadrob/F1-Prediction>`_ and click the green code drop-down button on the top left. From the drop down copy the `https` link which will use in a later step.
        
        .. image:: /images/clone.jpg

        3.  Once you have Git installed on your machine, create a folder where you would like the project to be checkedout to and open a Git bash terminal (`right-click` and `Git Bash Here`). Type in the bash terminal `git clone <repo-url>` for example: 
        
        .. image:: /images/cloneCommand.jpg
        
        4.  Once this command completes it will have cloned the F1 Predict repository to your local machine.


    -   Install Python

        1.  This project was developed in the `Python programming language <https://www.python.org/>`_ that is easier to pick up and has some powerful features that assist with various topics such as image modification, Machine Learning, and Artificial intelligence (AI). To install Python on your local machine navigate to `Python Installer <https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe>`_ which will start the download for you. 
        
        .. note:: **IMPORTANT: Please make sure you download python version 3.7 or lower. Any version higher than 3.7 is incompatible with the tkinter library**
        
        2.  Once the installer has downloaded you can open it
        
        .. image:: /images/py1.jpg
        
        3.  Select the custom installation option, check the boxs next to the tools you would like to include, **ensure you install pip** and click next, 
        
        .. image:: /images/py2.jpg
        
        .. note:: **IMPORTANT: Please make sure you add pip to your python installation.**
        
        4.  **Select 'add python to enviroment variables'**, then select where you would like to install python and finally click install
        
        .. image:: /images/py3.jpg
        
        .. note:: **IMPORTANT: Please make sure you add Python to your system PATH enviroment variable.** To manually add Python to your enviroment variables please look at this guide: `Add Pthon To Enviroment Variables <https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows>`_.
        
        5.  You can varify that the installation was successful by opening up a command line terminal and executing the `py -3.7` command as below:
        
        .. code:: 

            C:\Users\rober> py -3.7
            Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
            >>>
            >>> exit()
    

    -   Pip Install Required Packages

        1.  As a general-purpose programming language, Python is designed to be used in many ways with many powerful packages that add even more functionality. Python has a standard package manager, called `pip`, which allows you to install and manage packages that aren’t part of the Python standard library. It should have been installed with your python installation in the previous step.
        2.  To install all the required packages necessary for running this project you can open up a command line terminal in the root folder of where you cloned the project and execute the following command:
        
        .. code:: 

            py -3.7 -m pip install -r requirements.txt
    
        .. image:: /images/pip.jpg
        
        .. note:: **IMPORTANT: If the pip install command fails then try reopening the command lind terminal as administrator.**


Windows 8.1 (32-bit + 64-bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   Steps to Install Git

        1.  To use this project you will need to use Git to clone the repository. Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package, via installer, or download the source code and compile it yourself. Navigate to the `Download Git <https://git-scm.com/download/win>`_ page and download the windows setup for your operating system to begin. 

        .. image:: /images/gitDownload.jpg

        2.  Open `F1-Predict Repository <https://github.com/Quadrob/F1-Prediction>`_ and click the green code drop-down button on the top left. From the drop down copy the `https` link which will use in a later step.
        
        .. image:: /images/clone.jpg

        3.  Once you have Git installed on your machine, create a folder where you would like the project to be checkedout to and open a Git bash terminal (`right-click` and `Git Bash Here`). Type in the bash terminal `git clone <repo-url>` for example: 
        
        .. image:: /images/cloneCommand.jpg
        
        4.  Once this command completes it will have cloned the F1 Predict repository to your local machine.


    -   Install Python

        1.  This project was developed in the `Python programming language <https://www.python.org/>`_ that is easier to pick up and has some powerful features that assist with various topics such as image modification, Machine Learning, and Artificial intelligence (AI). To install Python on your local machine navigate to `Python Installer <https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe>`_ which will start the download for you. 
        
        .. note:: **IMPORTANT: Please make sure you download python version 3.7 or lower. Any version higher than 3.7 is incompatible with the tkinter library**
        
        2.  Once the installer has downloaded you can open it
        
        .. image:: /images/py1.jpg
        
        3.  Select the custom installation option, check the boxs next to the tools you would like to include, **ensure you install pip** and click next, 
        
        .. image:: /images/py2.jpg
        
        .. note:: **IMPORTANT: Please make sure you add pip to your python installation.**
        
        4.  **Select 'add python to enviroment variables'**, then select where you would like to install python and finally click install
        
        .. image:: /images/py3.jpg
        
        .. note:: **IMPORTANT: Please make sure you add Python to your system PATH enviroment variable.** To manually add Python to your enviroment variables please look at this guide: `Add Pthon To Enviroment Variables <https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows>`_.
        
        5.  You can varify that the installation was successful by opening up a command line terminal and executing the `py -3.7` command as below:
        
        .. code:: 

            C:\Users\rober> py -3.7
            Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
            >>>
            >>> exit()
    

    -   Pip Install Required Packages

        1.  As a general-purpose programming language, Python is designed to be used in many ways with many powerful packages that add even more functionality. Python has a standard package manager, called `pip`, which allows you to install and manage packages that aren’t part of the Python standard library. It should have been installed with your python installation in the previous step.
        2.  To install all the required packages necessary for running this project you can open up a command line terminal in the root folder of where you cloned the project and execute the following command:
        
        .. code:: 

            py -3.7 -m pip install -r requirements.txt
    
        .. image:: /images/pip.jpg
        
        .. note:: **IMPORTANT: If the pip install command fails then try reopening the command lind terminal as administrator.**


Windows 10 (32-bit + 64-bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   Steps to Install Git

        1.  To use this project you will need to use Git to clone the repository. Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package, via installer, or download the source code and compile it yourself. Navigate to the `Download Git <https://git-scm.com/download/win>`_ page and download the windows setup for your operating system to begin. 

        .. image:: /images/gitDownload.jpg

        2.  Open `F1-Predict Repository <https://github.com/Quadrob/F1-Prediction>`_ and click the green code drop-down button on the top left. From the drop down copy the `https` link which will use in a later step.
        
        .. image:: /images/clone.jpg

        3.  Once you have Git installed on your machine, create a folder where you would like the project to be checkedout to and open a Git bash terminal (`right-click` and `Git Bash Here`). Type in the bash terminal `git clone <repo-url>` for example: 
        
        .. image:: /images/cloneCommand.jpg
        
        4.  Once this command completes it will have cloned the F1 Predict repository to your local machine.


    -   Install Python

        1.  This project was developed in the `Python programming language <https://www.python.org/>`_ that is easier to pick up and has some powerful features that assist with various topics such as image modification, Machine Learning, and Artificial intelligence (AI). To install Python on your local machine navigate to `Python Installer <https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe>`_ which will start the download for you. 
        
        .. note:: **IMPORTANT: Please make sure you download python version 3.7 or lower. Any version higher than 3.7 is incompatible with the tkinter library**
        
        2.  Once the installer has downloaded you can open it
        
        .. image:: /images/py1.jpg
        
        3.  Select the custom installation option, check the boxs next to the tools you would like to include, **ensure you install pip** and click next, 
        
        .. image:: /images/py2.jpg
        
        .. note:: **IMPORTANT: Please make sure you add pip to your python installation.**
        
        4.  **Select 'add python to enviroment variables'**, then select where you would like to install python and finally click install
        
        .. image:: /images/py3.jpg
        
        .. note:: **IMPORTANT: Please make sure you add Python to your system PATH enviroment variable.** To manually add Python to your enviroment variables please look at this guide: `Add Pthon To Enviroment Variables <https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows>`_.
        
        5.  You can varify that the installation was successful by opening up a command line terminal and executing the `py -3.7` command as below:
        
        .. code:: 

            C:\Users\rober> py -3.7
            Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
            >>>
            >>> exit()
    

    -   Pip Install Required Packages

        1.  As a general-purpose programming language, Python is designed to be used in many ways with many powerful packages that add even more functionality. Python has a standard package manager, called `pip`, which allows you to install and manage packages that aren’t part of the Python standard library. It should have been installed with your python installation in the previous step.
        2.  To install all the required packages necessary for running this project you can open up a command line terminal in the root folder of where you cloned the project and execute the following command:
        
        .. code:: 

            py -3.7 -m pip install -r requirements.txt
    
        .. image:: /images/pip.jpg
        
        .. note:: **IMPORTANT: If the pip install command fails then try reopening the command lind terminal as administrator.**


Windows 11 (32-bit + 64-bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    -   Steps to Install Git

        1.  To use this project you will need to use Git to clone the repository. Before you start using Git, you have to make it available on your computer. Even if it’s already installed, it’s probably a good idea to update to the latest version. You can either install it as a package, via installer, or download the source code and compile it yourself. Navigate to the `Download Git <https://git-scm.com/download/win>`_ page and download the windows setup for your operating system to begin. 

        .. image:: /images/gitDownload.jpg

        2.  Open `F1-Predict Repository <https://github.com/Quadrob/F1-Prediction>`_ and click the green code drop-down button on the top left. From the drop down copy the `https` link which will use in a later step.
        
        .. image:: /images/clone.jpg

        3.  Once you have Git installed on your machine, create a folder where you would like the project to be checkedout to and open a Git bash terminal (`right-click` and `Git Bash Here`). Type in the bash terminal `git clone <repo-url>` for example: 
        
        .. image:: /images/cloneCommand.jpg
        
        4.  Once this command completes it will have cloned the F1 Predict repository to your local machine.


    -   Install Python

        1.  This project was developed in the `Python programming language <https://www.python.org/>`_ that is easier to pick up and has some powerful features that assist with various topics such as image modification, Machine Learning, and Artificial intelligence (AI). To install Python on your local machine navigate to `Python Installer <https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe>`_ which will start the download for you. 
        
        .. note:: **IMPORTANT: Please make sure you download python version 3.7 or lower. Any version higher than 3.7 is incompatible with the tkinter library**
        
        2.  Once the installer has downloaded you can open it
        
        .. image:: /images/py1.jpg
        
        3.  Select the custom installation option, check the boxs next to the tools you would like to include, **ensure you install pip** and click next, 
        
        .. image:: /images/py2.jpg
        
        .. note:: **IMPORTANT: Please make sure you add pip to your python installation.**
        
        4.  **Select 'add python to enviroment variables'**, then select where you would like to install python and finally click install
        
        .. image:: /images/py3.jpg
        
        .. note:: **IMPORTANT: Please make sure you add Python to your system PATH enviroment variable.** To manually add Python to your enviroment variables please look at this guide: `Add Pthon To Enviroment Variables <https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows>`_.
        
        5.  You can varify that the installation was successful by opening up a command line terminal and executing the `py -3.7` command as below:
        
        .. code:: 

            C:\Users\rober> py -3.7
            Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
            Type "help", "copyright", "credits" or "license" for more information.
            >>>
            >>> exit()
    

    -   Pip Install Required Packages

        1.  As a general-purpose programming language, Python is designed to be used in many ways with many powerful packages that add even more functionality. Python has a standard package manager, called `pip`, which allows you to install and manage packages that aren’t part of the Python standard library. It should have been installed with your python installation in the previous step.
        2.  To install all the required packages necessary for running this project you can open up a command line terminal in the root folder of where you cloned the project and execute the following command:
        
        .. code:: 

            py -3.7 -m pip install -r requirements.txt
    
        .. image:: /images/pip.jpg
        
        .. note:: **IMPORTANT: If the pip install command fails then try reopening the command lind terminal as administrator.**


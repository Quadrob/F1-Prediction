.. _troubleshoot:

Troubleshooting 
===============
This application is on its very first iteration and thus it may contain some issues. This section includes concise documentation for the end-user and potential software administrators to help if they encounter issues with software or hardware when running this application. 

Frequently Asked Questions
--------------------------

-   What is the F1 Predict application?

    -   This application is purely centered around Formula 1 and predicting outcomes of the sporting spectical. For a more detaied description please see the :ref:`overview` page for an overview or the :ref:`requirements` page for a list of features.

-   Do I have to pay to use the application?

    -   This application is completly free and licensed under the `GNU Free Documentation License <https://www.gnu.org/licenses/fdl-1.3.html>`_ act.

-   How do I use the application?

    -   This application is designed with a very simple UI and to find more detailed instructions regarding startup of the application please visit :ref:`installing` or for more detailed usage instructions please visit the :ref:`usage` page.

-   How do I install this application?

    -   This application is pretty easy to install and run, please visit the :ref:`installing` page for more deetails.

-   I can't pip install the required packages.

    -   Pip package manager cannot install packages if:
        
        -   You are not running the terminal as admin
        -   You have poor network connection
        -   You have a different pip / python version installe previously
        -   You don't have python configured in your enviroment variables

-   How do I add Python to my enviroment variables?

    -   It can be done automatically for you by the python installer or you can view these manual steps at `How To Add Python To Your Enviroment Variables <https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows>`_.

-   Where can I download Python?

    -   You can download the Python installer directly from the `Python.io Downloads <https://www.python.org/downloads/>`_ website.

    .. note:: **IMPORTANT:** Please ensure you download `Python 3.7 <https://www.python.org/downloads/release/python-379/>`_ version, furthure installation instructions can be found on the :ref:`installing` page.

-   I already have a different version of python installed.

    -   That is not a problem, if your currently installed python is 3.7 then continue using that version. If it is a version greater or lower than 3.7 then please download the `Python 3.7 <https://www.python.org/downloads/release/python-379/>`_ installer.

    .. note:: **IMPORTANT:** There could be conflicts with multiple versions of python installed if you do not manage your enviroment variables. Ensure Python 3.7 appears highest in your PATH enviroment variable and PYTHONHOME variable is set to Python 3.7.

-   How do I open a command line terminal as admin?

    -   There are multiple ways to open a terminal as admin, simplest is to search `CMD` and open as administrator. Other methods are detailed at `Admin CMD <https://www.educative.io/answers/how-to-run-cmd-as-an-administrator>`_ page.

-   What are the requirements to run this application?

    -   This is detailed on the :ref:`installing` page.

-   The F1 Predict application fails to start up.

    -   There are multiple reasons that this could occur, please have a look and the terminal window to see an error message and refer to the error message section below.

-   I am getting strange errors when I try to run the application.

    -   Please have a look at the error message section below, if you have a different error you are welcome to contact me, try the third-party resources, or fially a web browser.

-   Can I contribute to the F1 Predict project?

    -   Yes you may, the methods of contribution are detailed on the :ref:`develop` page.

-   How can I contact the developer of F1 Predict?

    -   You can contact me via email or other platforms, please see the :ref:`contact` page.

-   When was the database last updated?

    -   Currently the database was last updated in December of 2022 (12/2022).

    .. note:: There is a plan to implement automatic update of the database on the :ref:`future` page


Error Messages
--------------
These are some of the error messages that users reported during testing:

-   Missing Python

.. figure:: /images/missingpython.png
   :alt: example of missing python install
   :align: center
    
   *This can be resolved by installing a version of python, if you have already installed python please check your enviroment variables*

-   Missing modules

.. figure:: /images/missingpip.png
   :alt: example of missing pip package 
   :align: center
    
   *This can be resolved by running py -3.7 -m pip install -r requirements.txt in the root folder of F1 Predict*

-   Incorrect versions

.. figure:: /images/wrongversion.png
   :alt: example of incorrect versions
   :align: center
    
   *This can be resolved by ensuring you have the correct python version installed and configured in your enviroment variables*

-   Admin Privilages:

.. figure:: /images/adminpip.png
   :alt: example of missing privilage premissions
   :align: center
    
   *This can be resolved by running the terminal as administrator*

.. note:: **IMPORTANT:** If these error messages do not match yours please feel free to contact me, search the third-party resources, or just browse the internet for the answers.


Additional Documentation
------------------------
Contact Support
~~~~~~~~~~~~~~~
You are welcome to contact me on any of the mediuns on the :ref:`contact` page

Third-Party Resources
~~~~~~~~~~~~~~~~~~~~~
These are resources that are exceptionally good and helping with source code issuse:

-   `<https://www.educative.io/explore>`_
-   `<https://docs.python.org/3.7/>`_
-   `<https://pip.pypa.io/en/stable/>`_
-   `<https://stackoverflow.com/>`_
-   `How to install Python on Windows <https://studyopedia.com/python3/install-python-on-windows-10/>`_
-   `Pip Install <https://note.nkmk.me/en/python-pip-install-requirements/#:~:text=Install%20packages%20with%20pip%3A%20%2Dr%20requirements.txt,-The%20following%20command&text=You%20can%20name%20the%20configuration,%2Fto%2Frequirements.txt%20.>`_


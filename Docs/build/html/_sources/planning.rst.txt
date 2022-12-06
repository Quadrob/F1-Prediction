.. planning

Planning
========
Deployment
----------
The following are necessary steps in order to clarify the project, delegate tasks, develop and design, and releasing the final application.

Deployment Instructions
~~~~~~~~~~~~~~~~~~~~~~~

1.  Meet with a user to understand the requirments of the application and define the five proficiences
2.  Provide project analysis gathered from step one
3.  User Action Phase (List of the overview of activities/sprints hypothetical proposal to be performed from design to deployment of the application)
4.  Project development
    -   Database setup
    -   Data collection
    -   Data analysis
    -   ML training & testing
    -   Backend development
    -   Frontend development
5.  Application Testing
6.  Application Launch
    -   Install all prerequisites
    -   Install the application
    -   Perform post-installation steps
    -   Perform verification tests

Assumptions
~~~~~~~~~~~~
Describtion of the assumptions about the current capabilities and use of the application when it is
released live. The appliction would have a place for users to:

*   The application should predict a drivers Qualifying position
*   The application should predict a drivers Qualifying time difference to the leader
*   The application should predict a drivers Race finishing position
*   The application should predict a drivers Championship finishing position
*   The application should predict a constructors highest of their two drivers Qualifying position
*   The application should predict a constructors highest of their two drivers Qualifying time difference to the leader
*   The application should predict a constructors highest of their two drivers Race finishing position
*   The application should predict a constructors Championship finishing position
*   The application should suggest the best constructor for a driver
*   The application should suggest the best two drivers for a constructor

Dependencies
~~~~~~~~~~~~
Dependencies that can hinder or slows process of deployment are:

-   Dependent on using Google sources or any type of open source resources
-   External libraries not in my control eg xgboost
-   Unavoidable change of plans
    -   Change of needs / Research fails / Implementation fails
-   Time management

Configuration Settings
~~~~~~~~~~~~~~~~~~~~~~

*   Ensure Python version 3.7 is installed 
*   Add Python to enviroment variables
*   Pip install all required labraries

.. note:: These settings might differ if future versions depending on future development

Deployment Scripts
~~~~~~~~~~~~~~~~~~
Currently this application does not use any deployment scripts

Test Plan
~~~~~~~~~

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

Troubleshooting
~~~~~~~~~~~~~~~
The application is relativly easy to debug and diagnose. To begi, look at the UI to see if there are any error messages or inconsistencies. If there are no clear signs have a look at the open terminal that is running the application for error messages. 

The most common errors occur due to version conflicts in Python and/or is libraries. For more troubleshooting information please have a look at the :ref:`troubleshoot`


Licensing
---------
This application is licensed by the `GNU Free Documentation License <https://www.gnu.org/licenses/fdl-1.3.html>`_.

This License applies to any manual or other work, in any medium, that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. Such a notice grants a world-wide, royalty-free license, unlimited in duration, to use that work under the conditions stated herein. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you". You accept the license if you copy, modify or distribute the work in a way requiring permission under copyright law.

A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (Thus, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.

The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License. If a section does not fit the above definition of Secondary then it is not allowed to be designated as Invariant. The Document may contain zero Invariant Sections. If the Document does not identify any Invariant Sections then there are none.

The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License. A Front-Cover Text may be at most 5 words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, that is suitable for revising the document straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup, or absence of markup, has been arranged to thwart or discourage subsequent modification by readers is not Transparent. An image format is not Transparent if used for any substantial amount of text. A copy that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML, PostScript or PDF designed for human modification. Examples of transparent image formats include PNG, XCF and JPG. Opaque formats include proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML, PostScript or PDF produced by some word processors for output purposes only.

The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.

The "publisher" means any person or entity that distributes copies of the Document to the public.

A section "Entitled XYZ" means a named subunit of the Document whose title either is precisely XYZ or contains XYZ in parentheses following text that translates XYZ in another language. (Here XYZ stands for a specific section name mentioned below, such as "Acknowledgements", "Dedications", "Endorsements", or "History".) To "Preserve the Title" of such a section when you modify the Document means that it remains a section "Entitled XYZ" according to this definition.

The Document may include Warranty Disclaimers next to the notice which states that this License applies to the Document. These Warranty Disclaimers are considered to be included by reference in this License, but only as regards disclaiming warranties: any other implication that these Warranty Disclaimers may have is void and has no effect on the meaning of this License.

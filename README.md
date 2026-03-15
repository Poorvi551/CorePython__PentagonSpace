# CorePython__PentagonSpace
Learnings of Core Python at Pentagon Space with Shashank Sir.

__________________________________________________________________

Python : Python is a high level interpreted programming lannguage. 

Compilation: Compilation is a proess of converting a program into a high level language to machine level language where the code is executed in a single shot.

Interpretation: Interpretation is a process of converting a program into a high level language to machine level language where the code is executed line by line.

* Python program is a line by line execution *

  Python is a 3 dimensional model:

                            OOPS
                             |
                             |
                       Python Supports
                           /   \
                          /     \
                Functions         Scripting

  _______________________________________________________

  * Object Orientation

    Object - is a real world Entity/Instance of class.

    Orientation -

                  | Point of view
    
                  | Perspective
    
                  | Alignment

* 3 Steps:

  1. Identify
  2.  Define
  3.   Classify
 
  _____________________________________________

                   Classify
                    /    \
                 has     does
       
          Ex:
       
                   Student
                    /   \
                   /     \
              name        study
              usn         sleep
              age         eat
  ______________________________________________

* Pycharm Installation

  _______________________________________________________________________________________________________________________________________

       1. Google -> search Pycharm download -> open 1st link -> select operating system e.g, windows, mac, linux -> click on download.
       2. Google -> search python 3 download -> open 1st link -> click on download.
  _______________________________________________________________________________________________________________________________________

* First Python Program:

  _____________________________________________________________
  
        print("Hello! Welcome to your Python Journey.")
  
  ______________________________________________________________


  * Object creation Program :-

    _________________________________________________________________________________________

        class Student:        # creating object
            name="Ram"
            usn="4fg67897"
            age=19
        def study():         # creation of method
            print("Ram is good in studying")
    
        #  This program throws an error because the constructor is not initialized.
  ____________________________________________________________________________________________

* The constructor/ Special method/ Init method :-

  ___________________________________________________________________________________________
  Syntax :-

         >> def __init__(self):

  __________________________________________________________________________________________

* Object creation Program :-

    _________________________________________________________________________________________

        class Student:              # creating object
            def __init__(self):
                name="Ram"
                usn="4fg67897"
                age=19
            def study():            # creation of method
            print("Ram is good in studying")
        s1=Student()
        print(s1.name)
        print(s1.usn)
        print(s1.age)
        s1.study()
        
    
        #  This program executes successfully because the constructor is initialized.
  ____________________________________________________________________________________________
    

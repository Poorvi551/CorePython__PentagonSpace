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

    Object - is a real world Entity / Instance of class.

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

* The constructor / Special method / Init method :-

  ___________________________________________________________________________________________
  Syntax :-

         >> def __init__(self):

  __________________________________________________________________________________________

* Object creation Program :-

    _________________________________________________________________________________________

        class Student:
            def __init__(self):
                self.name="Poorvi"
                self.age=21
                self.usn="4SH22IS050"
            def study(self):
                print("Poorvi is studying")
            def walk(self):
                print("Poorvi is walking")
            def sleep(self):
                print("Poorvi is sleeping")
            def eat(self):
                print("Poorvi is eating")
       s1=Student()
       print(s1.name)
       print(s1.age)
       print(s1.usn)
       s1.study()
       s1.walk()
       s1.sleep()
       s1.eat()
        
        #  This program executes successfully because the constructor is initialized.
  ____________________________________________________________________________________________
  Source code File - student.py

  * Output :-
  ___________________________________________________________________________________________

      C:\Users\poorvinayak\AppData\Local\Microsoft\WindowsApps\python3.12.exe "C:\Users\poorvinayak\OneDrive\Documents\Core python\student.py" 
      Poorvi
      21
      4SH22IS050
      Poorvi is studying
      Poorvi is walking
      Poorvi is sleeping
      Poorvi is eating

      Process finished with exit code 0

_________________________________________________________________________________________________________

Similar object creation files - heroobj.py

* NOTE : The complete python code is controlled and coordinated by PVM (Python Virtual Machine)

How the backend works?!

* PVM creates a separate block of memory with an address.
* Then it searches for a constructor once it found the constructor the address will be stored in the self keyword.Later the complete data will be stored in that separate block of memory.
* The address of an object will be stored in one reference variable and that is pointing out to the same memory location.

* Organization of RAM :

  1. Code Segment.
  2. Static Segment.
  3. Stack Segment.
  4. Heap Segment.

Actual Creation of an object




    
    

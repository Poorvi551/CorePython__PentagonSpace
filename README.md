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

  1. Code Segment - stores Program.
  2. Static Segment - stores static variable.
  3. Stack Segment - stores local variable.
  4. Heap Segment - stores object.

** Actual Creation of an object:

Source code : heroobj.py

How the backend works?!

* PVM creates a separate block of memory in a heap segment with an address.
* Then it searches for a constructor once it found the constructor the address will be stored in the self keyword.Later the complete data will be stored in that separate block of memory.
* The address of an object will be stored in one reference variable and the reference variable will be stored in the stack segment and that is pointing out to the same memory location.

* Adding, Modifying and Deleting the values outside class:

  * Source code - heroineobj.py

* Adding : adding values
  
   * syntax - ex: h1.movies="PK"   ( consider heroineobj.py file )

* Modifying : changing existing values

   * syntax - ex: h1.age=34      ( consider heroineobj.py file )

* Deleting : Removing values

   * syntax - ex: del h1.numOfMovies  ( consider heroineobj.py file )

* Printing Address Value of an object :-

   * syntax - ex: print(h1)      ( consider heroineobj.py file )
   
Data types and variables:-

  * Variable - Variable is a container that is used to store the values.
  * Variables are used to identify and access values from the memory or RAM.

    * syntax: var = val

       * ex: a = 10

Rules for naming variables :

1. Variable name should start with either letters or underscore.
2. Variable name should not contain only numbers and should not start with numbers.
3. Variable name should not contain any special characters except underscore.
4. Variable name cannot be the keywords.
5. Variable name cannot contain any spaces. Ex: na me
6. Varaible name can contain A-Z, a-z and 0-9.Ex: Name123, Name, name
7. Variables are case sensitive.

   ** NOTE : In python variable are considered as an object.
   ** NOTE : In python data size is not fixed.

* Conditional Statements :  Statements that check for the conditions and going to exeecute the code.

  1. if -->T, F
  2. elif -->T, F
  3. else

* Input Statements :

   Stetements that are used to take input values from user.
  
   * Ex:
     
             a = input("Enter a num:")
             b = input("Enter a num:")  
             print(a)
             print(b)
             c = a+b    # concatenates the numebers - join
             print(c)

To overcome this or to add the values we use - * int(input)

  Source Code files in repo -  >> intinput.py

* Greater than program using input statements and condition statements.
  
   * Source Code files in repo -  >> intinput.py

* Looping Statements :
  
   * They are :

       1. For Loop
       2. While Loop

  1. For Loop :

      * Syntax
     _______________________________________________________________________
     
           for var_name in list_of_elements:
     _______________________________________________________________________

     Ex : source code - forloop.py

  *  Range() :

    Built in function in python.
     * They are of three types :
         1. range(stop)
         2. range(start,stop)
         3. range(start,stop,step)
     
  3. While Loop :

      * Syntax
    __________________________________________________________________________

            while condtion:
    __________________________________________________________________________
  
  Ex : source code - while.py

* Various ways of declaring instance variable :-

 Three ways :
  1. Inside the constructor  -  using self keyword
  2. Inside the method    -  using self keyword
  3. Outside the constructor  -  using referrence variable

* Methods -

  * Method is a behaviour of an object and it will work when it is called.

  * Types of methods(3 types) :-
      1. Instance method
             1. No parameter No return Value
             2. No parameter with return Value
             3. With parameter No return Value
             4. With parameter with return Value
      2. Static method
      3. Class method
         
1. Instance method:

     Syntax:
     _______________________________________________________________

         def __methodname__(self):
             _________________
             _________________
             [code here]______
             _________________
     ________________________________________________________________

     1. No parameter No return Value :

        Ex: source code - calcinopnorv.py

     2. No parameter with return value :

        Ex : source code - calcinopwithrv.py
        
     3. With parameter no return value :

        Ex : source code - calciwithpnorv.py

     4. With parameter with return value :

        Ex: source code - calciwithpwithrv.py

2. Static method :

    Syntax:
   ________________________________________________________

        @static method
        def methodname():
           _______________
           _______________
   ________________________________________________________

3. Class method :

    Syntax:
   _________________________________________________________

        @class method
        def methodname(cls):
           _______________
           _______________
   __________________________________________________________

  Ex : source code : carmethod.py

* Method returning multiple values:-

   * If we are not declaring a constructor the PVM will declare one default constructor at the backend.
   * Ex : source code : methodretnmultival.py

* Standard way of declaring a class :

  

  
        

     
    







    
    

# CorePython__PentagonSpace
Learnings of Core Python at Pentagon Space with Shashank Sir.

__________________________________________________________________

**Python** : Python is a high level interpreted programming lannguage. 

**Compilation**: Compilation is a proess of converting a program into a high level language to machine level language where the code is executed in a single shot.

**Interpretation**: Interpretation is a process of converting a program into a high level language to machine level language where the code is executed line by line.

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

## **Object Orientation**

    **Object** - is a real world Entity / Instance of class.

    ***Orientation*** -

                  | Point of view
    
                  | Perspective
    
                  | Alignment

#### **3 Steps**:

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

## ***Pycharm Installation***

  _______________________________________________________________________________________________________________________________________

       1. Google -> search Pycharm download -> open 1st link -> select operating system e.g, windows, mac, linux -> click on download.
       2. Google -> search python 3 download -> open 1st link -> click on download.
  _______________________________________________________________________________________________________________________________________

#### *First Python Program*:

  _____________________________________________________________
  
        print("Hello! Welcome to your Python Journey.")
  
  ______________________________________________________________


#### *Object creation Program* :-

    _________________________________________________________________________________________

        class Student:        # creating object
            name="Ram"
            usn="4fg67897"
            age=19
        def study():         # creation of method
            print("Ram is good in studying")
    
        #  This program throws an error because the constructor is not initialized.
  ____________________________________________________________________________________________

#### *The constructor / Special method / Init method* :-

  ___________________________________________________________________________________________
  Syntax :-

         >> def __init__(self):

  __________________________________________________________________________________________

#### *Object creation Program* :-

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
  *Source code File - [student.py](./student.py)*

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

*Similar object creation files - [heroobj.py](./heroobj.py)*

***NOTE : The complete python code is controlled and coordinated by PVM (Python Virtual Machine)***

*How the backend works?!*

* PVM creates a separate block of memory with an address.
* Then it searches for a constructor once it found the constructor the address will be stored in the self keyword.Later the complete data will be stored in that separate block of memory.
* The address of an object will be stored in one reference variable and that is pointing out to the same memory location.

*Organization of RAM :*

  1. Code Segment - stores Program.
  2. Static Segment - stores static variable.
  3. Stack Segment - stores local variable.
  4. Heap Segment - stores object.

**Actual Creation of an object:**

*Source code : [heroobj.py](./heroobj.py)*

*How the backend works?!*

* PVM creates a separate block of memory in a heap segment with an address.
* Then it searches for a constructor once it found the constructor the address will be stored in the self keyword.Later the complete data will be stored in that separate block of memory.
* The address of an object will be stored in one reference variable and the reference variable will be stored in the stack segment and that is pointing out to the same memory location.

### **Adding, Modifying and Deleting the values outside class:**

*Source code - [heroineobj.py](./heroineobj.py)*

 * **Adding** : adding values
  
   * *syntax* - ex: h1.movies="PK"   ( consider [heroineobj.py](./heroineobj.py) file )

 *  **Modifying** : changing existing values

   * *syntax* - ex: h1.age=34      ( consider [heroineobj.py](./heroineobj.py) file )

 *  **Deleting** : Removing values

   * *syntax* - ex: del h1.numOfMovies  ( consider [heroineobj.py](./heroineobj.py) file )

 * Printing Address Value of an object :-

   *syntax* - ex: print(h1)      ( consider [heroineobj.py](./heroineobj.py) file )

## **Data types and variables:-**

  **Variable** - Variable is a container that is used to store the values.
  * Variables are used to identify and access values from the memory or RAM.

    *syntax:* var = val

       * ex: a = 10

### **Rules for naming variables :**

1. Variable name should start with either letters or underscore.
2. Variable name should not contain only numbers and should not start with numbers.
3. Variable name should not contain any special characters except underscore.
4. Variable name cannot be the keywords.
5. Variable name cannot contain any spaces. Ex: na me
6. Varaible name can contain A-Z, a-z and 0-9.Ex: Name123, Name, name
7. Variables are case sensitive.

   **NOTE : In python variable are considered as an object.**
   **NOTE : In python data size is not fixed.**

### **Conditional Statements :**  

  * Statements that check for the conditions and going to exeecute the code.

  1. if -->T, F
  2. elif -->T, F
  3. else

**Input Statements :**

  * Statements that are used to take input values from user.
  
   * Ex:
     
             a = input("Enter a num:")
             b = input("Enter a num:")  
             print(a)
             print(b)
             c = a+b    # concatenates the numebers - join
             print(c)

To overcome this or to add the values we use - * int(input)

  Source Code files in repo -  >> [intinput.py](./intinput.py)

* Greater than program using input statements and condition statements.
  
   * Source Code files in repo -  >> [intinput.py](./intinput.py)

## * **Looping Statements :**
  
   * They are :

       1. For Loop
       2. While Loop

### **1. For Loop :**

  * Syntax
     _______________________________________________________________________
     
           for var_name in list_of_elements:
     _______________________________________________________________________

     Ex : source code - [forloop.py](./forloop.py)

###  *  **Range() :**

  Built in function in python.
     * They are of three types :
         1. range(stop)
         2. range(start,stop)
         3. range(start,stop,step)
     
###  **3. While Loop :**

 * Syntax
    __________________________________________________________________________

            while condtion:
    __________________________________________________________________________
  
  Ex : source code - [while.py](./while.py)

* Various ways of declaring instance variable :-

 Three ways :
  1. Inside the constructor  -  using self keyword
  2. Inside the method    -  using self keyword
  3. Outside the constructor  -  using referrence variable

### * **Methods -**

  * Method is a behaviour of an object and it will work when it is called.

  *  **Types of methods(3 types) :-**
    
      1. Instance method
             1. No parameter No return Value
             2. No parameter with return Value
             3. With parameter No return Value
             4. With parameter with return Value
      2. Static method
      3. Class method

**1. Instance method:**


     Syntax:
     _______________________________________________________________

         def __methodname__(self):
             _________________
             _________________
             [code here]______
             _________________
     ________________________________________________________________

   1. No parameter No return Value :

        Ex: source code - [calcinopnorv.py](./calcinopnorv.py)

   2. No parameter with return value :

        Ex : source code - [calcinopwithrv.py](./calcinopwithrv.py)
        
   3. With parameter no return value :

        Ex : source code - [calciwithpnorv.py](./calciwithpnorv.py)

  4. With parameter with return value :

        Ex: source code - [calciwithpwithrv.py](./calciwithpwithrv.py)

**2. Static method :**

  Syntax:
   ________________________________________________________

        @static method
        def methodname():
           _______________
           _______________
   ________________________________________________________

**3. Class method :**

  Syntax:
   _________________________________________________________

        @class method
        def methodname(cls):
           _______________
           _______________
   __________________________________________________________

  *Ex : source code : [carmethod.py](./carmethod.py)*

* **Method returning multiple values:-**

   * If we are not declaring a constructor the PVM will declare one default constructor at the backend.
   * Ex : source code : [methodretnmultival.py](./methodretnmultival.py)

* **Standard way of declaring a class :**

  Ex: Source code - [standardwaystudent.py](./standardwaystudent.py), (Similar ex: [Farmer.py](./Farmer.py))

* **Static variable:-**

  * **Declaration :**

     * Static Variables are declared inside the class outside the constructor.
     * To access static variables we have to use classname.

       * Ex:

             class farmer:
                 r=2.5
                 def __init__(self,p,t,r):
                     _______________
                     _______________

         Ex: source code - [staticfarmer.py](./staticfarmer.py)

#### * **Actual Parameter and Formal Parameter.**

   * *Ex Source code : [demoparameters.py](./demoparameters.py)*

               class Demo:
                   def add(self,a,b):  # a, b here are Formal Parameter
                       c=a+b
                       print(c)
               d1=Demo()
               x=10
               y=20
               d1.add(x,y)            # here x, y are Actual Parameter

#### * **Keywords and arguments :**

  Ex : Source code :- [parameters.py](./parameters.py)

#### * **High cohension and Low cohension:-**

  * High Cohension - If the properties and behaviour are related to the objects is called High cohension.
  * Ex: source code -
 
  * Low Cohension - If the properties and behaviour is not related to the objects is called High cohension.
  * Ex: source code -
    
  * In python main block will start from first line and it will end at last line and this main block is called suite.

## Strings

 * Strings - String is a collection or sequence of characters.
 * Major feature of string - Immutable.
 * Strings are stored in global dictionary in the backend.

#### * **Indexing:**

 * They are of two types :
    1. Positive indexing (moves from left -> right)
    2. Negative indexing (moves from right -> left)

 #### * **Operations :**

 * Operations are of 4 types:
    1. Arithmetic operators - (+,-,*,/,**,//)
    2. Logical operators - (and, or, not)
    3. Relational or comparison operator - (==,!=, >, <, >=, <=)
    4. Assignment operator - (=, +=, -=, *=, /=)

 #### * **String slicing:**

  * ***Slicing*** - Slicing extracts multiple characters.
    
  * *Syntax:*
      Ex:

        str="RajaRamMohanRoy"
        print(str.slice[2:6])  // prints str from index 2 to 6-1 =5 index

   *Ex: Source code : [slice.py](./slice.py)*

   * **Rules for slicing :-**

     1. Irrespective of starting and ending values check for the step value.
          * If step value is :
              * +ve -> positive indexing -> left to right.
              * -ve -> negative indexing -> right to left
     2. If initially we found the :
         * starting value -> then we will get the output
         * ending value -> no output
     3. If the step value is 0 -> throws an error

 ### * **Strip():**

  * Strip -  Removes the whitespaces in the beginning and ending of the string.
  * lstrip() -  Removes the whitespaces in the beginning.
  * rstrip() - Removes the whitespaces in the ending.

#### ** ***Reverse a string program.***

    def reverse_string(s):
        rev=''
        for i in s:
            rev=i+rev
        return rev
    s=input("Enter a string:")
    print(reverse_string(s))

#### ** ***Reverse a sentence using split method:***

    str = "Ahalya is writing"
    str1=str.split()
    print(str)
    print(str1)
    rev=''
    for i in str:
        rev=i+""+rev
        print(rev)

### * **Split() -**

* Split - splits the sentence once it finds the whitespace and store it in the form of list.

#### ** ***Palindrome program:***

    def palindrome(str):
        rev=""
        for i in str:
            rev=i+rev
            print(rev)
        if str==rev:
            print("String is palindrome")
        else:
            print("String is not a palindrome")

### * **Lowercase, Uppercase and Swapcase:-**

 * .lower() - converts the  string to lowercase
 * .upper() - converts the  string to uppercase
 * .swapcase() - converts the string to lowercase or uppercase or mixed case based on the input.
 *  *Ex - Source code - [stringcase.py](./stringcase.py)*

** ***Finding the substring from the given string:-***

 * Ex: source code - [substring.py](./substring.py)
   
       str="if you think you can or you can't, you are right"
       print(str)
       str1="you"
       print(str1 in str)
       print(str.count("you"))
       print(str.index("you"))
       print(str.find("you"))
       print(str.rindex("you"))
       print(str.rfind("you"))
       print(str.find("pentagon"))
       print(str.index("pentagon"))

### * Check alphabets,numbers, or other special characters present in string. 

* *Ex :- Source code -  checkchardigit.py

* **.isalpha** - checks if the string contains only alphabets.
* **.isdigit** - checks if the string contains only digits or numbers.
* **.isalnum** - checks if the string contains bothe alphabets and numbers.

### * Packing and unpacking :-

* **Packing** - Storing the sequence of elements in a single variable is called packing.
* **unpacking** - Storing the sequence of elements in the separate variable is called unpacking.

* *Ex :- Source code - [packunpack.py](./packunpack.py)*

### * **ASCII Values :-**

* ASCII Value - ASCII (American Standard Code for Information Interchange)

*  *A - 65* , *Z - 90*
*  *a - 97* , *z - 122*
*  *space (' ') - 32*

** Check ASCII Values:-

* *Ex :- Source code - [ascii.py](./ascii.py)*

      alpha=input("Enter a alphabet:")
      res1=ord(alpha)            # prints number of alphabet
      print(res1)
      num=int(input("Enter a number:"))
      res2=chr(num)             # prints chr of alphabet
      print(res2)

  * ord() - prints the  ASCII value of the alphabet.
  * chr() - prints the  ASCII value of the number.

### * **Replacing a string :-**

* *Ex :- source code - [replacestring.py](./replacestring.py)*

      str="Shaky is scanning"
      print(str)
      str1=str.replace("is","was")
      print(str1)
      print(str.startswith("Shaky"))   #True
      print(str.startswith("Rahul"))   #False
      print(str.endswith("scanning"))  #True
      print(str.endswith("Shaking"))   #Falsenterning

* Replace() - replaces a new string instead of old string which you want to replace.

### * **String Interning:-**

* *Ex :- source code - [stringInterning.py](./stringInterning.py)*

* String Interning : It is an internal memory optimization technique in Python. Checks for the same element, if same element present multiple times then assigns the same memory address to that particular element. 

### * **Formatting String :-**

* Format string - String formatting refers to assign value taken from the user to print anything.
  
* *Ex: Source code - [formatstring](./formatstring)*

## Functions

### * **Funtion :-** A Function is a set or block of code which performs a specific task when it is called.

* Syntax :-

      def fun_name()
          ______________
          ______________
      fun_name()          # calling function.

* ***NOTE - Function will not work unless you call it.***

* Difference between method and function

<table>
  <tr>
    <center>
      <td>METHODS</td>
      <td>FUNCTIONS</td>
    </center>
  </tr>
  <tr>
    <td>Declared inside the class.</td>
    <td>Declared directly without class.</td>
  </tr>
  <tr>
    <td>Use self keyword.</td>
    <td>No need of self keyword.</td>
  </tr>
  <tr>
    <td>To call method we require referrence variable.</td>
    <td>In functions no need of referrence variable.</td>
  </tr>
  <tr>
    <td>Dependent of class.</td>
    <td>Independent of lass.</td>
  </tr>
</table>

### * **Types of functions :-**

  1. No parameter no return value.
  2. No parameter with return value.
  3. With parameter no return value.
  4. With parameter with return value.

 ### **1. No parameter no return value :-**

  * *Ex- Source code - [nopnorv.py](./nopnorv.py)*

        def add():
            a=10
            b=20
            c=a+b
            print(c)
        add()

 ### **2. No parameter with return value :-** 

 * *Ex- Source code - [nopwithrv.py](./nopwithrv.py)*
   
       def add():
            a=10
            b=20
            c=a+b
            return c
        res=add()
        print(res)
   
### **3. With parameter no return value :-**

* *Ex- Source code - [withpnorv.py](./withpnorv.py)*

       def add(a,b):
            c=a+b
            print c
        x=17
        y=36
        add(x,y)
  
 ### **4. With parameter with return value :-**

 * *Ex- Source code - [withpwithrv.py](./withpwithrv.py)*

       def add(a,b):
            c=a+b
            return c
        x=17
        y=36
        res=add(x,y)
        print(res)

   ### * **Invoking Functions through variable :-**

  ### ***NOTE :- The address of the function is stored i the function name.***

  * *Ex- Source code - [invokefunctions.py](./invokefunctions.py)*

  ### * **Global variable :-**

  * * *Ex- Source code - [globalvariable.py](./globalvariable.py)*
   
  ### * **Accessing global variable with or without using global :-**

  * *Ex- Source code - [globalvar.py](./globalvar.py)*

## * **Nested Function :-**

### ***NOTE :- In a nested function we have to call inner function inside the outer function outside the inner function.***

* *Ex- Source code - [nestedfun.py](./nestedfun.py)*

      def outer():
          print("Inside outer")
          def inner():
              print("Inside inner")
          inner()
      outer()

### * **Higher order function and first class function:-**

* The function which accepts another function as parameter is called as higher order function.
* Other than higher order function all are first class function.

* *Ex :- Source code - [highorderfun.py](./highorderfun.py)*

### * **Non-Local variables:-**

* In a nested function the variable present in the most inner function is called as local variable remaining all the variable will act as non local variable.
* *Ex:- Source code - [nonlocalvar.py](./nonlocalvar.py)*

### * **LEGB Rule:-**

L - Local Scope
E - Enclosed Scope
G - Global Scope
B - Built in Scope

### * **Lambda Function :-**

* It is a anonymous function with easy syntax for small operations.
* Syntax:

       lambda arguments : expresssion
  
* *Ex:- Source code - [lambda.py](./lambda.py)*

### * Modules :-*

* Module is a pyton file where we can import code from one module to another module and we can use it.
* *Ex :- Source code(folder) - [module](./module) ,[modul2](./modul2)

* Importing both [p1.py](./p1.py), [p2.py](./p2.py) file in [new1.py](./new1.py) file.

**  ***Collect 5 integer values from the user and store it in a list or arr.***

    l=[]
    i=0
    while i<=4:
        num=int(input("Enter Numbers:")
        l.insert(i,num)
        i+=1
    print(l)

### * **Filtering and Mapping:-**

<table>
  <tr>
    <td>Filtering</td>
    <td>Output < Input</td>
  </tr>
  <tr>
    <td>Mapping</td>
    <td>Output == Input with different values</td>
  </tr>
</table>

### * **Filtering :-**

* It is a built in function in python which is used to filter the values and this is the best example for higher order function.
* *Ex:- Source code - [filterfun.py](./filterfun.py)*
* Using lambda function.
* *Ex:- Source code - [lambdfilter.py](./lambdfilter.py)*

### * **Mapping :-**

* It is a built in function in python which is used to map the values and this is also the best example for hiher order function.
* *Ex:- Source code - [map.py](./map.py)*

### * **Closure :-**

* Closure - In a nested function calling inner function outside the outer function.
* *Ex:- Source code -

      def outer():
          print("Inside outer")
          def inner():
              print("Inside inner")
          return inner
      ref=outer()
      ref()

### * **Decorators:-**

* Decorators - Accessing code from one function to another function and if we want we can modify it will not affect to the main function/main code.
* *Ex:- Source code - [decorators.py](./decorators.py)

      def main():
          print("Inside main function")
      def outer(ptr):
          print("Inside outer function")
          def inner():
              print("Inside inner function")
              ptr()
              print("Leaving inner function")
      ref=outer(main)
      ref()

### * **Accessing and modifying the non local variables :-**

* *Ex:- Source code - [accessnonlocal.py](./accessnonlocal.py)*

## **Generators :-**

* Generators - It is a function which generates the sequence of values  with the help of *yield* keyword.
* If any function which consists of minimum of one *yield* keyword inside it is called as "Generator".

### * **next() :-**

* It is used to retrieve next item from a generator.
* This will resume the execution from the last, until it reaches the next one.

### * **yield keyword:-**

* **Yield -**  This will pause the execution of a function by saving its current state.
  
### ***NOTE :- When there are no values inside the henerator if we use next function it will throw an error. the error is "stop iteration error".

** Difference between generators and functions.

<table>
  <tr>
    <td>Functions</td>
    <td>Generators</td>
  </tr>
  <tr>
    <td>It returns only single value using 'return keyword'</td>
    <td>It returns multiple values using 'yield keyword'</td>
  </tr>
  <tr>
    <td>Store entire data in a memory.</td>
    <td>Generates values lazily in demand.</td>
  </tr>
  <tr>
    <td>Function can be slow for large data</td>
    <td>Generators are more efficient for large data.</td>
  </tr>
</table>

* *Ex :- Source code - [generator.py](./generator.py)*

      def generator():
          yield 1
          yield 2
          yield 3
      res=generator()
      print(res)
      print(next(res))

# OOPS 

### * ***OOPS - Object Oriennted Programming System***

### * Pillers of python (OOPs) :-

  1. Encapsulation
  2. Inheritance
  3. Polymorphism
  4. Abstraction

## **1. Encapsulation :-**

* *Encapsulation* - Providing controlled access to the private members of the class , in simple we can call it as binding of the data.
* To provide security we have some access modifiers :-
* There are 3 types of access modifiers :
     1. public - self.pages - (without ( _ ) underscore)
     2. protected - self._pages - (with ( ._ ) single underscore)
     3. private - self.__pages - (with ( .__ ) double underscore)


      class Book:
           def __init__(self,pages):
               self.__page=pages            # public self converted to private
      b1=Book(100)
      print(b1.__pages)

  * In the above program we have converted the public variable into private variable by applying  __ ( double underscore).
  * The private variables cannot be accessed directly even by the developer.
  * To acces private variables we have to use 2 methods they are:
       1. setter()
       2. getter()
  * *Ex :- Source code - [encapsulation.py](./encapsulation.py)*
 
        class Book:
            def __init__(self,pages):
                self.__page=pages            # public self converted to private
            def setter(self,val):
                if val>0:
                    self.__page=val
            def getter(self):
                return self.__page
        b1=Book(100)
        b1.setter(200)
        res=b1.getter()
        print(res)

## * **Normal Encapsulation :-**

* *Ex :- Source code - [personnormencapsulation.py](./personnormencapsulation.py)*

## * **Property() Encapsulation :-**

* *Ex :- Source code - [getsetencap.py](./getsetencap.py)*
  

      class Book:
            def __init__(self):
                self.__page=""            # public self converted to private
            def getter(self):
                return self.__page
            def setter(self,pages):
                self.__page=pages
            getset=property(getter,setter)
      b1=Book(100)
      b1.getset=200
      res=b1.getset
      print(res)

## * **@Property() Decorators Encapsulation :-** 

* ***NOTE :- 1. Only in a normal encapsulation we have to call both setter and getter method.***
          ***2. In remaining two types of encapsulation we don't need to cal just we have to assign values.***

* *Ex :- Source code - [propertyencap.py](./propertyencap.py)*
    
      class Person:
           def __init__(self):
               self.__pname=""            # public self converted to private
           @property
           def dispName(self):
               return self.__page
           @dipName.setter
           def dispName(self,names):
               self.__pname=names
      p1=Person(100)
      p1.dispName="ABC"
      res=b1.dispNmae
      print(res)
  
### * ***Converting public method into private method :-***

    class Car:
         def __init__(self):
             self.brand=""
         def __move(self):
             print("Car is moving")
    c1=Car()
    c1.__move()                       # Attribute Error

### * ***NOTE:- To access private method we have to use one helper method and this method should be in public mode.***

    class Car:
         def __init__(self):
             self.brand=""
         def __move(self):
             print("Car is moving")
         def helper(self):
             self.__move()
    c1=Car()
    c1.helper()

## **2. Inheritance :-**

* Inheritance - It is a mechanism which allows us to inherit the properties and behaviours from one class to another class.(Parent - child)
* Derived class - It is also called child class.

* ***NOTE :- In Inheritance object is created only for the class which acts as a child class.***

### * **Super() :-**

 * It is used to connect the parent class constructor to the child class constructor without using classname.
 * *Ex:- Source code - [supermethod.py](./supermethod.py)*

       class A:
           def __init__(self):
               self.a=10
       class B(A):
           def __init__(self):
               super().__init__()
               self.b=20
       class C(B):
           def __init__(self):
               super().__init__()
               self.c=30
       c1=C()
       print(c1.c)
       print(c1.b)
       print(c1.a)

### * ***Implementation of Inheritance :-***

**UML Diagram :- (Unified Modelling Language)**

<img width="1280" height="960" alt="WhatsApp Image 2026-06-20 at 11 30 17 AM" src="https://github.com/user-attachments/assets/c7be8bd4-ee62-470a-94a4-ac84d60d5a63" />

## **Types of Inheritance :-**

1. Single level inheritance
2. Multi level inheritance
3. Hierarchical inheritance
4. Multiple inheritance
5. Hybrid inheritance

### **1. Single level inheritance :-**

* Single parent single child
* *Ex :- Source code - [](./)*

      class A:
           def disp_A(self):
               print("In A")
      class B(A):
           def disp_B(self):
               print("In B")
      b1=B()
      b1.disp_B()
      b1.disp_A()

### **2. Multi level inheritance :-**

* A new child class is derived from already existing derived class is called Multi level inheritance.
* *Ex:- Source code -*

      class A:
           def disp_A(self):
               print("In A")
      class B(A):
           def disp_B(self):
               print("In B")
      class C(B):
           def disp_C(self):
               print("In C")
      c1=C()
      c1.disp_C()
      c1.disp_B()
      c1.disp_A()
   

   








    
    

  
         
  

  

  
        

     
    







    
    

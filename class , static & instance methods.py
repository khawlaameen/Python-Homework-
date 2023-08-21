'''
class methods vs static methods:
   * class methods:
        *The class method takes cls (class) as first argument.
        *Class method can access and modify the class state.
        *The class method takes the class as parameter to know about the state of that class.
        *@classmethod decorator is used.
   * Syntax for Class Method.

       class my_class:
           @classmethod 
           def function_name(cls, arguments): 
               Function Body...
               return value 

***********************************************************************************
    * static methods:
        *The static method does not take any specific parameter.
        *Static Method cannot access or modify the class state.
        *Static methods do not know about class state.
        *@staticmethod decorator is used.
        
    * Syntax for Static Method.
       class my_class: 
           @staticmethod 
           def function_name(arguments): 
               Function Body... 
               return value 
           
***********************************************************************************
     *instance methods:
        * instance methods can freely access attributes and other 
        * methods on the same object.
        * This gives them a lot of power when it comes to modifying an object’s state.
        * Not only can they modify object state, 
         instance methods can also access the class itself through the self.classattribute. 
        *This means instance methods can also modify class state.
        
     * Syntax for Instance Method.
       class my_class: 
           def function_name(self, arguments): 
               Function Body... 
               return value 
        
'''

# Define class method 
class Counter: 
    counter = 0 
    def __init__(self,name): 
        self.name = name 
        Counter.counter += 1 
    @classmethod 
    def display_count(cls): 
        print("The count is:", cls.counter) 
obj1 = Counter("Khawla") 
obj2 = Counter("Nora") 
Counter.display_count() 



# Define static method 

class Employee(object):
    
    @staticmethod
    def gather_requirement(name,project_name):
        if project_name == 'FD_Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        print(requirement)

Employee.gather_requirement("Khawla","FD_Project")


# Define instance method 

class MyClass: 
    name="khawla"
    def method(self):
        self.name="fatom"
        print("instance method called and can access the class attribute and modefiy it to ",self.name)

obj = MyClass()
obj.method() 


"""
Event-Driven Programming ^_^

In computer programming, event-driven programming is a programming paradigm in
 which the flow of the program is determined by events such as user actions
 (mouse clicks, key presses), sensor outputs, or message passing from other
 programs or threads. Event-driven programming is the dominant paradigm used
 in graphical user interfaces and other applications 
 (e.g., JavaScript web applications) that are centered on performing certain
 actions in response to user input. This is also true of programming for device
 drivers (e.g., P in USB device driver stacks.
In an event-driven application, there is generally a main loop that listens for
 events and then triggers a callback function when one of those events is detected.
 In embedded systems, the same may be achieved using hardware interrupts instead 
 of a constantly running main loop. Event-driven programs can be written in any 
 programming language, although the task is easier in languages that provide
 high-level abstractions, such as await and closures.


"""

#Name: Pratham Ramkripal Yadav  
#Date: 08  
#Assignment: Lab 10
#Class: CPS 596



#Question 1: Defining a Base Class
#Define a class Vehicle with properties like make, model, and year. Use self in __init__
#Create a method display_info() that prints out this information.

#Defining Class Vehicle
class Vehicle:
    #Initializing the Vehicle class
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    #Defining display_info() method to print the values
    def display_info(self):
        print("Make : ", self.make)
        print("Model : ",self.model)
        print("Year : ", self.year)

# Example Usage
print("\n----------- Question 1 -----------\n")
v = Vehicle('Toyota', 'Corolla', 2020)
v.display_info()

#Question 2: Simple Inheritance
#Define a class Car that inherits from Vehicle and adds a property wheels with a default value of 4. (How does a class inherit from another class)
#Override the display_info() method to include the number of wheels. (i.e. what else needs to be added to display_info)

#Defining Car Class Inherited for Vehicle Class 
class Car(Vehicle):
    #Default values go here
    #Initializing the Car class
    def __init__(self,make,model,year,wheels=4):
        super().__init__(make,model,year)
        self.wheels=wheels

    #Defining display_info() function 
    def display_info(self):
        super().display_info()
        print("Wheels : ", self.wheels )

# Example Usage
print("\n----------- Question 2 -----------\n")
c = Car('Honda', 'Civic', 2019)
c.display_info()


#Question 3: Constructor Chaining
#Define a class ElectricCar that inherits from Car. Add a new property battery_size. Ensure that the constructor properly uses super() to initialize the inherited properties.
#Polymorphism and Dynamic Behavior

#Defining ElectricCar Class Inherited for Car Class 
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make,model,year)
        self.battery_size=battery_size

# Example Usage
print("\n----------- Question 3 -----------\n")
ec = ElectricCar('Tesla', 'Model 3', 2021, '75kWh')
ec.display_info()
print(f'Battery size: {ec.battery_size}')


#Question 4: Method Overriding
#Demonstrate method overriding by defining a method charge() in both Vehicle (doing nothing or raising a NotImplementedError) 
#and ElectricCar (where it actually performs a relevant action, like updating a battery_level attribute).
#Instantiate electriccar and print charge

#Defining Vehicle Class 
class Vehicle:
    # ... (other methods and properties)
    def charge(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

#Defining ElectricCar Class Inherited for Car Class 
class ElectricCar(Car):
    # ... (other methods and properties)
    def charge(self):
        self.battery_level=100

# Example Usage
print("\n----------- Question 4 -----------\n")
ec = ElectricCar('Tesla', 'Model S', 2022, '100kWh')
ec.charge()


#Question 5: Multiple Inheritance
#Two base classes are defined: Electric and Hybrid, with their own unique methods and properties. 
#Create a class HybridElectricCar that inherits from both and call both functions that are inherited.

#Defining Electric Class 
class Electric:
    def charge(self):
        print("Charging electric component.")

#Defining Hybrid Class 
class Hybrid:
    def fill_tank(self):
        print("Filling the tank.")

#Defining HybridElectricCar Class inherited from Hybrid and Electric
class HybridElectricCar(Hybrid,Electric):
    
    def MultipleInheritance(self):
        super().charge()
        super().fill_tank()

# Example Usage - call both functions here
hec = HybridElectricCar()
hec.MultipleInheritance()

#Question 7b: Multiple inheritance. Which method gets called from C?
#Answer: Method do_something() in Class B gets called
class A:
    def do_something(self):
        print("Method defined in A")

class B(A):
    def do_something(self):
        print("Method defined in B")

class C(B, A):
    pass
    

# Example usage
c_instance = C()
c_instance.CcallsMethod()
#We will leran about an object lifecycle

#Define a class
class Bike:
    count = 0
    name =''
    def __init__(self,n): #Constructor is automatically called when u create na instance of an object,remeber to give 2 underscores
        self.name=n     #bike must have a name
        print(f"{self.name} bike instance created ")
    def __del__(self):
        """Destructor is called when an oject isntance is of no use, 
           although, desctructor is not required,python automatically
           takes cares of this.
        """
        print(f"{self.name} is getting destroyed")
        
    def honk(self):          #A general method, always remeber to pass self as argumen or it throws error
        self.count+=1
        print(f"Honk!!! count incresed to {self.count}")


#create an instance
s = Bike("Sam")            #Create an object of class Bike   
s.honk()
s.honk()
s=42                     #object is destroyed as s is now pointing to int class object

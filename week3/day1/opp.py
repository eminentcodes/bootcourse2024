class Car():
    def __init__(self,name,price):
        self.name = name 
        self.price = price

    def rename_Car(self,new_name):
        self.name = new_name
    def presentation_Car(self):
        print(f"\n the name of my car is {self.name} and the price is ${self.price}")
    

    def remise(self,percentage):
        return(self.price- (self.price  * percentage)/ 100)




def Print_my_name(self):
    print(f"\n my name is {self.name} \n")
def Print_my_price(self):
     print(f"\n my price is ${self.price} \n")

        
        

my_first_car = Car('toyota',2000)
my_second_car = Car('mercedes',15000)
my_third_car = Car('bmw',7000)


my_first_car.presentation_Car()
my_second_car.rename_Car ('range rover')
my_third_car.presentation_Car()


my_second_car.Print_my_price()
my_second_car.remise (50)
my_second_car.Print_my_price()



print(f"\n the name of my first car is {my_first_car.name} and the price is ${my_first_car.price}")
print(f"\n the name of my second car is {my_second_car.name} and the price is ${my_second_car.price}")
print(f"\n the name of my  third car is {my_third_car.name} and the price is ${my_third_car.price}")
  


    







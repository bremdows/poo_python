class Cooking :
    def __init__(self, type) :
        self.__temperature = 0
        self.type = type 
    
    # Utilizando el decorador property para definir los setters and getters
    @property
    def temperature(self) :
        "This is the temperature to cook the ingredients for the food" # This is the documentation
        
        return self.__temperature

    @temperature.setter
    def set_temperature(self, new_temperature) :
        if new_temperature < 0 :
            raise ValueError("Don't cook with temperatures lower to 0")
        else :
            print("We have a new temperature to cook")
            self.__temperature = new_temperature
    
    @temperature.deleter
    def del_temperature(self) :
        print("temperature atribute was delete")
        del self.__temperature

saltado = Cooking("Medium fire")
print("Method of cook is:", saltado.type)
saltado.set_temperature = 20
print("The temperature to cook the Lomo Saltado is:",saltado.temperature,"Cº")
del saltado.del_temperature


    

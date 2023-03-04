#class with methods to compute temperature change in celcius and fahrenheits
class Temperature:
        def __init__(self,temperature):
            self.temperature=temperature
        def convert_fahrenheit(self):
            return (self.temperature*1.8)+32
        def convert_celcius(self):
            return(self.temperature-32)/1.8
f=Temperature(30)
print(f.convert_fahrenheit())
print(f.convert_celcius())

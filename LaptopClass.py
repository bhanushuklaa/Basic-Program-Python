#Create a Laptop with Attribute like Brand name, Model name, Price
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.rate = price
a=Laptop('Lenovo', 'ASdf4512', 450000)
print(a.brand)
print(a.model)
print(a.rate)
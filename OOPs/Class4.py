class Laptop:
    def __init__ (self,brand,ram):
        self.brand=brand
        self.ram=ram

laptop1=Laptop("Lenova","16 GB")

print("Brand:",laptop1.brand)
print("Ram:",laptop1.ram)
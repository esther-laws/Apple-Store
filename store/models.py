from django.conf import settings
from django.db import models
from django.utils import timezone

class Selection:
    def __init__(self, Device, Sales_Data, User_Data):
        self.Device = Device
        self.Sales_data = Sales_Data
        self.User_data = User_Data

class Device(Selection):
    def __init__(self, Phone, Tablet, Laptop):
        self.Phone = Phone
        self.Tablet = Tablet
        self.Laptop = Laptop

class Phone(Device):
    def __init__(self, pmake, pmodel, pyear, pstorage):
        self.pmake = pmake
        self.pmodel = pmodel
        self.pyear = pyear
        self.pstorage = pstorage

phones = [
    {
        "pmake": "Apple iPhone",
        "pmodel": "iPhone SE (2nd Gen)",
        "pyear": "2022",
        "pstorage": "64GB, 128GB, 256GB"
    },
    {
        "pmake": "Apple iPhone",
        "pmodel": "iPhone 13",
        "pyear": "2021",
        "pstorage": "128GB, 256GB, 512GB"
    },
    {
        "pmake": "Apple iPhone",
        "pmodel": "iPhone 14",
        "pyear": "2022",
        "pstorage": "128GB, 256GB, 512GB"
    },
    {
        "pmake": "Apple iPhone",
        "pmodel": "iPhone 15",
        "pyear": "2023",
        "pstorage": "128GB, 256GB, 512GB"
    },
    {
        "pmake": "Apple iPhone",
        "pmodel": "iPhone 15 Pro",
        "pyear": "2023",
        "pstorage": "128GB, 256GB, 512GB, 1TB"
    }
]

for phone in phones:
    print(f"Make: {phone['pmake']}")
    print(f"Model: {phone['pmodel']}")
    print(f"Year: {phone['pyear']}")
    print(f"Storage Options: {phone['pstorage']}")
    print("\n")

class Tablet(Device):
    def __init__(self, dmake, dmodel, dyear, dstorage):
        self.dmake = dmake
        self.dmodel = dmodel
        self.dyear = dyear
        self.dstorage = dstorage

tablets = [
    {
        "dmake": "Apple iPad",
        "dmodel": "iPad Mini",
        "dyear": "2021",
        "dstorage": "64GB, 256GB"
    },
    {
        "dmake": "Apple iPad",
        "dmodel": "iPad (10th Gen)",
        "dyear": "2022",
        "dstorage": "64GB, 256GB"
    },
    {
        "dmake": "Apple iPad",
        "dmodel": "iPad Air (5th Generation)",
        "dyear": "2022",
        "dstorage": "64GB, 256GB"
    },
    {
        "dmake": "Apple iPad",
        "dmodel": "iPad Pro (6th Generation)",
        "dyear": "2023",
        "dstorage": "128GB, 256GB, 512GB, 1TB, 2TB"
    }
]

for tablet in tablets:
    print(f"Make: {tablet['dmake']}")
    print(f"Model: {tablet['dmodel']}")
    print(f"Year: {tablet['dyear']}")
    print(f"Storage Options: {tablet['dstorage']}")
    print("\n")

class Laptop:
    def __init__(self, lmake, lmodel, lyear, lstorage):
        self.lmake = lmake
        self.lmodel = lmodel
        self.lyear = lyear
        self.lstorage = lstorage

laptops = [
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Pro 16'(M2 Max and M2 Pro)",
        "lyear": "2023",
        "lstorage": "1TB, 2TB, 4TB, 8TB"
    },
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Pro 14'(M2 Max and M2 Pro)",
        "lyear": "2023",
        "lstorage": "512GB, 1TB, 2TB, 4TB, 8TB"
    },
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Pro 13'(M2 Chip)",
        "lyear": "2022",
        "lstorage": "256GB, 512GB, 1TB, 2TB"
    },
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Air 15' (M2 Chip)",
        "lyear": "2023",
        "lstorage": "256GB, 512GB, 1TB, 2TB"
    },
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Air 13' (M2 Chip)",
        "lyear": "2022",
        "lstorage": "256GB, 512GB, 1TB, 2TB"
    },
    {
        "lmake": "Apple MacBook",
        "lmodel": "MacBook Air 13' (M1 Chip)",
        "lyear": "2020",
        "lstorage": "256GB, 512GB, 1TB, 2TB"
    }
]

for laptop in laptops:
    print(f"Make: {laptop['lmake']}")
    print(f"Model: {laptop['lmodel']}")
    print(f"Year: {laptop['lyear']}")
    print(f"Storage Options: {laptop['lstorage']}")
    print("\n")

class Sales_Data(Selection):
    def __init__(self, gross, cost, quantity):
        self.gross = gross
        self.cost = cost
        self.quantity = quantity

    def calculate_profit(self):
        return self.gross - self.cost
    
if __name__ == "__main__":
    try:
        gross = float(input("Enter total sales gross: "))
        cost = float(input("Enter total cost: "))
        quantity = int(input("Enter quantity sold: "))

        sales_data = Sales_Data(gross, cost, quantity)
        profit = sales_data.calculate_profit()

        username = "John Doe"
        items_in_cart = ["Phone", "Tablet", "Laptop"]
        total_price = gross - cost

        print(f"Username: {username}")
        print(f"Items in Cart: {', '.join(items_in_cart)}")
        print(f"Total: ${total_price}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for cost, and quantity.")
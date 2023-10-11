
class customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

       
class wares:
    def __init__(self,amount, item, price) -> None:
        self.amount = amount
        self.item = item
        self.price = price

class purchases:
    def __init__(self,customer,ware,price) -> None:
        self.customer = customer
        self.ware = ware
        self.price = price
        
    def purchase(self):
        pass

def main():
    pass
    
    
if __name__ == "__main__":
    main()

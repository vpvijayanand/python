#Encapsulation
class Computer:
    def __init__(self):
        self.__max_price = 900  # Private attribute

    def sell(self):
        return f"Selling Price: {self.__max_price}"

    def set_max_price(self, price):
        if price > self.__max_price:
            self.__max_price = price

# Create an instance
c = Computer()

# Try changing the price
c.set_max_price(1000)
print(c.sell())

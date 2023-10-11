import random
import time

class Stocks:
    def __init__(self, name: str, nick: str, start_value: float):
        self.name = name
        self.nick = nick
        self.start_value = start_value
        self.current_price = start_value

    def simulate(self, ticks_per_hour=12, total_ticks=24 * 12):
        for tick in range(1, total_ticks + 1):
            
            percentage_change = random.uniform(-2, 2)
            
            self.current_price += (self.current_price * (percentage_change / 100))
            
            if self.current_price < 0:
                self.current_price = 0
            
            hours = tick // ticks_per_hour
            minutes = (tick % ticks_per_hour) * 5
            print(f'Time: {hours:02}:{minutes:02} Stock: {self.name} ({self.nick}) '
                  f'Price: ${self.current_price:.2f} Percentage Change: {percentage_change:.2f}%')
            
            time.sleep(5)

def main():
    stock = Stocks(name="Tesla", nick="TSLA", start_value=10)

    stock.simulate()

if __name__ == "__main__":
    main()
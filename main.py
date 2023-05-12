import sys
sys.path.append(r'./cmd')
from chatGPT import chatGPT
from get import GetStock

class StockGPT:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def readAPI(self):      
        sys.path.append(r'./a')   
        with open('config', 'r') as f:
            for i in f.readlines():
                if "#" in i:
                    continue
                elif "gptAPI=" in i:
                    self.api_key = i.strip("gptAPI=").strip("\n")
                    print("api key:",self.api_key)
                

    def get(self):
        stock = GetStock(self.stock_code)
        stock.run()
        self.day = stock.getStockDay()
        self.month = stock.getStockMonth()

    def analyze(self,price):
        analyze = chatGPT(self.api_key, price)
        return analyze.analyze_price()

    def run(self):
        self.readAPI()
        self.get()
        anDay = self.analyze(self.day)
        anMonth = self.analyze(self.month)
        print("Estimated stock price tomorrow:",anDay)
        print("Estimated stock price next month:",anMonth)





if __name__ == "__main__":
    stock = input("Please enter the stock code:")
    app = StockGPT(stock)
    app.run()


class GetStock:
    def __init__(self,code):
        self.code = code

            
    def getStockInfo(self):
        import yfinance as yf
        import pandas as pd
        import datetime as dt
        
        start_date = dt.datetime.now() - dt.timedelta(days=365)
        end_date = dt.datetime.now()
        
        stock_data = yf.download(self.code, start=start_date, end=end_date)
        
        self.stock_data = stock_data
    
        
    def getStockDay(self):
        last_30_days = self.stock_data.tail(30)
                
        close_data = last_30_days['Close'].tolist()

        return close_data

        
    def getStockMonth(self):
        month_data = self.stock_data.resample('M').last()
        close_data = month_data['Close'].tolist()
        return close_data

    def run(self):
        self.getStockInfo()



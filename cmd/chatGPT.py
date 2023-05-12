import openai

class chatGPT:
    def __init__(self,api,price):
        self.api = api
        self.price = price
    
        
    def analyze_price(self):
        response = openai.Completion.create(

            engine="text-davinci-002",

            prompt=f"根据这组数据预测列表里的下一项: {self.price}。请直接输出结果，不需要其他文字！",

            max_tokens=1024,

            n=1,

            stop=None,

            temperature=0.5,

            api_key=self.api
        )
        return response
    

    def main(self):
        # Your main function code here
        price = self.analyze_price()
        return price

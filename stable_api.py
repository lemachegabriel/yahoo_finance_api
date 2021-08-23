import requests 

class Api:
    def __init__(self, quote, range, interval):
        self.SESSION = requests.Session()
        self.HEADER = {"User-Agent": r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
        self.QUOTE = quote
        self.RANGE = range
        self.INTERVAL = interval
    
    def send_request(self):
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{self.QUOTE}?region=US&lang=en-US&includePrePost=false&interval={self.INTERVAL}&useYfid=true&range={self.RANGE}&corsDomain=finance.yahoo.com&.tsrc=finance"
        self.data = self.SESSION.get(url, headers=self.HEADER)
        return self.data
   
    @property
    def open(self):
        data = self.send_request().json()
        return data["chart"]["result"][0]["indicators"]["quote"][0]["open"]

    @property
    def close(self):
        data = self.send_request().json()
        return data["chart"]["result"][0]["indicators"]["quote"][0]["close"]

    @property
    def high(self):
        data = self.send_request().json()
        return data["chart"]["result"][0]["indicators"]["quote"][0]["high"]

    @property
    def low(self):
        data = self.send_request().json()
        return data["chart"]["result"][0]["indicators"]["quote"][0]["low"]




print(Api("WEGE3.SA", "1mo", "1d").close, "CLOSE")
print(Api("WEGE3.SA", "1d", "1d").open, "OPEN")
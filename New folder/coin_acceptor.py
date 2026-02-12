# coin_acceptor.py

class CoinAcceptor:
    def __init__(self):
        self.amount = 0      # تعداد سکه‌های وارد شده
        self._value = 1.0    # ارزش هر سکه (می‌توان ثابت 1 واحد در نظر گرفت)

    def insertCoin(self) -> None:
        """یک سکه وارد می‌شود"""
        self.amount += 1

    def getAmount(self) -> int:
        """مقدار فعلی سکه‌ها را برمی‌گرداند"""
        return self.amount

    def returnCoins(self) -> int:
        """تمام سکه‌ها را برمی‌گرداند و شمارنده را صفر می‌کند"""
        coins = self.amount
        self.amount = 0
        return coins

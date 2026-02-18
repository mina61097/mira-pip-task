class CoinAcceptor:
    def __init__(self):
        self.__amount: int = 0
        self.__value: float = 0.0

    def insertCoin(self, coin: float) -> None:
        """Insert a coin with given value."""
        self.__amount += 1
        self.__value += float(coin)

    def getAmount(self) -> int:
        return self.__amount

    def getValue(self) -> float:
        return self.__value

    def returnCoins(self) -> tuple[int, float]:
        """Return (amount, value) and reset the acceptor."""
        amount = self.__amount
        value = self.__value

        self.__amount = 0
        self.__value = 0.0

        return amount, value

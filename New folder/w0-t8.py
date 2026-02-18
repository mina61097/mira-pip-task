
    class CoinAcceptor:
    def __init__(self):
        self.__amount: int = 0   # number of coins inserted
        self.__value: float = 0.0  # total value of coins

    def insertCoin(self, coin: float) -> None:
        """Insert a coin with given value."""
        self.__amount += 1
        self.__value += coin

    def getAmount(self) -> int:
        """Return the number of coins currently inserted."""
        return self.__amount

    def getValue(self) -> float:
        """Return the total value of inserted coins."""
        return self.__value

    def returnCoins(self) -> tuple[int, float]:
        """Return all coins and their total value, then reset the acceptor."""
        amount = self.__amount
        value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return amount, value
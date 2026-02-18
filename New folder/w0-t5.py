class CoinAcceptor:
    def __init__(self):
        # private properties
        self.__amount: int = 0
        self.__value: float = 0.0  # optional: total monetary value

    def insertCoin(self) -> None:
        self.__amount += 1
        self.__value += 1.0  # assuming each coin is worth 1.0

    def getAmount(self) -> int:
        return self.__amount

    def returnCoins(self) -> int:
        returned = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return returned

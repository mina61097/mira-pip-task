class CoinAcceptor:
    def __init__(self):
        self.__coins_count = 0
        self.__total_value = 0.0

    def insert_coin(self, value: float):
        """Insert a coin and update count and total value."""
        self.__coins_count += 1
        self.__total_value += value
        print("Inserting...")
        print(f"Inserted coins = {self.__coins_count}, value = {self.__total_value}€\n")

    def returnCoins(self) -> tuple[int, float]:
        """Return inserted coins as a tuple and reset counters."""
        coins = self.__coins_count
        value = self.__total_value
        self.__coins_count = 0
        self.__total_value = 0.0
        return coins, value

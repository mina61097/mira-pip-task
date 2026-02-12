class Counter:
    def __init__(self):
        self.__count = 0  # initialize count to 0

    def addCount(self) -> None:
        """Increment the count by 1."""
        self.__count += 1

    def getCount(self) -> int:
        """Return the current count."""
        return self.__count

    def zeroCount(self) -> None:
        """Reset count to 0."""
        self.__count = 0

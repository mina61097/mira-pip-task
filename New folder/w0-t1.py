class Counter:
    def __init__(self):
        # private property
        self.__count: int = 0

    def addCount(self) -> None:
        self.__count += 1

    def getCount(self) -> int:
        return self.__count

    def zeroCount(self) -> None:
        self.__count = 0

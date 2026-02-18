class TemperatureConverter:
    def __init__(self):
        # private property
        self.__temperature: float = 0.0  # stored as Celsius by default

    def setTemperature(self, temp: float) -> None:
        self.__temperature = float(temp)

    def toCelsius(self) -> float:
        return self.__temperature

    def toFahrenheit(self) -> float:
        return (self.__temperature * 9 / 5) + 32

    def toKelvin(self) -> float:
        return self.__temperature + 273.15

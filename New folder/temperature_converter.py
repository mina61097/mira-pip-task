# temperature_converter.py

class TemperatureConverter:
    def __init__(self):
        self.temperature = 0.0  # مقدار اولیه دما

    def setTemperature(self, temp: float) -> None:
        """مقدار دما را تنظیم می‌کند"""
        self.temperature = temp

    def toCelsius(self) -> float:
        """دما را به سانتی‌گراد تبدیل می‌کند"""
        # فرض می‌کنیم مقدار temperature بر حسب سانتی‌گراد است
        return self.temperature

    def toFahrenheit(self) -> float:
        """دما را به فارنهایت تبدیل می‌کند"""
        return (self.temperature * 9/5) + 32

    def toKelvin(self) -> float:
        """دما را به کلوین تبدیل می‌کند"""
        return self.temperature + 273.15

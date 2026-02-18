# =========================================
# Base Class
# =========================================

class SmartDevice:
    def __init__(self, device_name, status="off"):
        self.device_name = device_name
        self.status = status

    def operate(self):
        """Override this method in subclasses"""
        raise NotImplementedError("Subclasses must implement operate()")


# =========================================
# Subclasses
# =========================================

class SmartLight(SmartDevice):
    def __init__(self, device_name, brightness=50, status="off"):
        super().__init__(device_name, status)
        self.brightness = brightness

    def operate(self):
        self.status = "on" if self.status == "off" else "off"
        print(f"{self.device_name} light is now {self.status} at brightness {self.brightness}")


class SmartThermostat(SmartDevice):
    def __init__(self, device_name, temperature=22, status="off"):
        super().__init__(device_name, status)
        self.temperature = temperature

    def operate(self):
        self.status = "on"
        print(f"{self.device_name} thermostat is set to {self.temperature}°C")


class SmartLock(SmartDevice):
    def __init__(self, device_name, locked=True):
        super().__init__(device_name, status="locked" if locked else "unlocked")
        self.locked = locked

    def operate(self):
        self.locked = not self.locked
        self.status = "locked" if self.locked else "unlocked"
        print(f"{self.device_name} lock is now {self.status}")


# =========================================
# Polymorphic Operation
# =========================================

def operate_all_devices(devices):
    if not devices:
        print("No devices added yet!")
        return
    print("\n--- Operating All Devices ---")
    for device in devices:
        try:
            device.operate()
        except Exception as e:
            print(f"Error operating {device.device_name}: {e}")


# =========================================
# Device Creation
# =========================================

def create_device():
    print("\nChoose device type:")
    print("1 - Smart Light")
    print("2 - Smart Thermostat")
    print("3 - Smart Lock")

    choice = input("Choice: ")
    name = input("Enter device name: ")

    if choice == "1":
        try:
            brightness = int(input("Enter brightness (0-100): "))
        except ValueError:
            brightness = 50
            print("Invalid brightness, defaulting to 50")
        return SmartLight(name, brightness)

    elif choice == "2":
        try:
            temperature = int(input("Enter temperature (°C): "))
        except ValueError:
            temperature = 22
            print("Invalid temperature, defaulting to 22°C")
        return SmartThermostat(name, temperature)

    elif choice == "3":
        return SmartLock(name)

    else:
        raise ValueError("Invalid device type selected.")


# =========================================
# Main Menu
# =========================================

def main():
    devices = []

    while True:
        print("\n===== Smart Home Menu =====")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                device = create_device()
                devices.append(device)
                print(f"{device.device_name} added!")

            elif choice == "2":
                operate_all_devices(devices)

            elif choice == "0":
                print("Exiting Smart Home System...")
                break

            else:
                print("Invalid menu choice. Try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

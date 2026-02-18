import csv


# ======================================
# Exceptions
# ======================================

class PipelineError(Exception):
    pass


class InvalidMenuChoice(PipelineError):
    pass


# ======================================
# Device Classes
# ======================================

class IoTDevice:
    device_type = "GENERIC"

    def __init__(self, device_id, location, data):
        self.device_id = device_id
        self.location = location
        self.data = data

    def serialize_row(self):
        return [self.device_type, self.device_id, self.location, str(self.data)]


class TemperatureSensor(IoTDevice):
    device_type = "TEMP"

    @staticmethod
    def from_row(row):
        return TemperatureSensor(row[1], row[2], float(row[3]))


class HumiditySensor(IoTDevice):
    device_type = "HUM"

    @staticmethod
    def from_row(row):
        return HumiditySensor(row[1], row[2], float(row[3]))


class MotionSensor(IoTDevice):
    device_type = "MOTION"

    @staticmethod
    def from_row(row):
        return MotionSensor(row[1], row[2], row[3] == "True")


DEVICE_TYPES = {
    "1": TemperatureSensor,
    "2": HumiditySensor,
    "3": MotionSensor
}


# ======================================
# Pipeline
# ======================================

class IoTDataPipeline:

    KEY = 123  # simple XOR key

    # ---------- Serialization ----------

    def serialize(self, devices, filename="devices.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["type", "id", "location", "data"])
            for d in devices:
                writer.writerow(d.serialize_row())

        print("Serialized to devices.csv")

    # ---------- Deserialization ----------

    def deserialize(self, filename="devices.csv"):
        devices = []

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                for cls in DEVICE_TYPES.values():
                    if cls.device_type == row[0]:
                        devices.append(cls.from_row(row))

        print("Deserialized successfully")
        return devices

    # ---------- Simple XOR Encryption ----------

    def _xor_process(self, data: bytes):
        return bytes([b ^ self.KEY for b in data])

    def encrypt(self, input_file="devices.csv", output_file="devices.enc"):
        with open(input_file, "rb") as f:
            data = f.read()

        encrypted = self._xor_process(data)

        with open(output_file, "wb") as f:
            f.write(encrypted)

        print("Encrypted -> devices.enc")

    def decrypt(self, input_file="devices.enc", output_file="devices_dec.csv"):
        with open(input_file, "rb") as f:
            data = f.read()

        decrypted = self._xor_process(data)

        with open(output_file, "wb") as f:
            f.write(decrypted)

        print("Decrypted -> devices_dec.csv")


# ======================================
# Menu
# ======================================

def add_device():
    print("\n1-Temperature  2-Humidity  3-Motion")
    choice = input("Choice: ")

    if choice not in DEVICE_TYPES:
        raise InvalidMenuChoice("Invalid device type.")

    device_id = input("Device ID: ")
    location = input("Location: ")
    data = input("Data: ")

    cls = DEVICE_TYPES[choice]

    if cls == MotionSensor:
        data = data.lower() == "true"
    else:
        data = float(data)

    return cls(device_id, location, data)


# ======================================
# Main
# ======================================

def main():
    pipeline = IoTDataPipeline()
    devices = []

    while True:
        print("\n===== IoT Data Pipeline =====")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")

        try:
            choice = input("Enter choice: ")

            if choice == "1":
                devices.append(add_device())

            elif choice == "2":
                pipeline.serialize(devices)

            elif choice == "3":
                devices = pipeline.deserialize()
                for d in devices:
                    print(vars(d))

            elif choice == "4":
                pipeline.encrypt()

            elif choice == "5":
                pipeline.decrypt()

            elif choice == "0":
                break

            else:
                raise InvalidMenuChoice("Invalid menu option.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

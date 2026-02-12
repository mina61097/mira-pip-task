class FileHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[str]:
        with open(self.filepath, "r", encoding="utf-8") as file:
            rows = file.readlines()
        return rows


def main():
    handler = FileHandler("inventory.csv")

    rows = handler.read()

    for row in rows:
        print(row.strip())


if __name__ == "__main__":
    main()

from coin_acceptor import CoinAcceptor

def main():
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing its value (0 returns the money, -1 exits the program)\n")

    coin_machine = CoinAcceptor()

    while True:
        try:
            user_input = input("Insert coin (0 return, -1 exit): ").strip()
            coin_value = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if coin_value == -1:
            print("\nExiting program.")
            break
        elif coin_value == 0:
            coins, value = coin_machine.returnCoins()
            print("Returning coins...")
            print(f"{coins} coin{'s' if coins != 1 else ''} with {value}€ value returned.")
            print(f"Inserted coins = 0, value = 0€\n")
        elif coin_value > 0:
            coin_machine.insert_coin(coin_value)
        else:
            print("Invalid coin value. Please insert a positive number, 0, or -1.\n")

    print("\nThank you for using the coin acceptor program.")
    print("Program ending.")

if __name__ == "__main__":
    main()

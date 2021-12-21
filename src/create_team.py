def start():
    print("")
    print("Welcome to the pokemon team maker thing.")
    print("-" * 20)
    print("Choose one of the options below to get started\n")
    print("0. Exit script")
    print("1. Add Pokemon to team")
    print("-" * 20)
    print("")
    user_choice = float("-inf")
    while user_choice != 0:
        user_choice = int(input("> "))
        print(user_choice)
    print("")
    print("Exiting script")


if __name__ == "__main__":
    start()

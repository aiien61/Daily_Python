def collatz(number: int) -> None:
    while True:
        if number == 1:
            break

        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
    
    return None


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter a number: "))
            collatz(number)
            break
        except ValueError:
            print("Invalid input. You did not type in a number.")
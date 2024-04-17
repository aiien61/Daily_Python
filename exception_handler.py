def spam(divide_by):
    try:
        print(f"{divide_by} -> {50 / divide_by}")
    except ZeroDivisionError:
        print("Error: Invalud argument. Can't divide by zero.")

def cat_numbers():
    try:
        num_cats = int(input("How many cats do you have? "))
        if num_cats >= 3:
            print("That is a lot of cats.")
        elif num_cats < 0:
            print('That is not possible to have negative number of cats.')
        else:
            print("That is not that many cats.")
    except ValueError:
        print('You did not enter a number.')



if __name__ == '__main__':
    spam(2)
    spam(10)
    spam(0)
    spam(1)
    cat_numbers()
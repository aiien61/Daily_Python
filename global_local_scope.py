eggs = 50 # global variable

def spam():
    global eggs
    eggs = 100 # local variable
    print('in local spamm eggs: ', eggs)

if __name__ == "__main__":
    print('global eggs: ', eggs)
    spam()
    print('global eggs again: ', eggs) # eggs has been changed

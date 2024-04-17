import pyperclip

if __name__ == "__main__":
    pyperclip.copy(input("say something: "))
    print(pyperclip.paste())

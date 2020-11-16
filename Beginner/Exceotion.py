# create variable and prompt a question to the user


while True:
    try:

        number = int(input("What`s your age?\n im whaithing,,,\n"))
        print(18 / number)
        break
    except:

        print("Make sure you add a number!!!\n is a bug!")

    finally:
        print("Program finished!")



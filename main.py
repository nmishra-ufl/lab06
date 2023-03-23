def encode(password):
    # Written by Nikhil Mishra
    new_password = ""
    for num in password:
        new_password += (str((int(num) + 3) % 10))
    return new_password


def main():
    password = ""
    print("Welcome to the super secure password encoder!")
    while True:
        print("_______________________________________\n1. Encode Password\n2. Decode Password\n3. Show Password\n4. Quit\n_______________________________________")
        selection = int(input("\nEnter a selection: "))
        if selection == 4:
            break
        elif selection == 1:
            password = input("Enter a password to be encoded: ")
            print(f"\nYour encoded password is: {encode(password)}")
        elif selection == 2:
            pass
        elif selection == 3:
            print(f"Your password is: {password}")



if __name__ == "__main__":
    main()

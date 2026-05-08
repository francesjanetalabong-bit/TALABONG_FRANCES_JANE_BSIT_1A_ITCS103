
def read_messages():
    try:
        with open("dreams.txt", "r") as file:
            content = file.read()

            if content.strip() == "":
                print("\nThe file is currently empty. No inspiring messages to Display")
                
            else:
                print("\n--- Inspiring Messages ---")
                print(content)
                print("--------------------------\n")

    except FileNotFoundError:
        print("\nThe file dreams.txt does not exist.\n")


def add_message():
    message = input("\nEnter your inspiring message: ")

    with open("dreams.txt", "a") as file:
        file.write(message + "\n")

    print("Message added successfully!\n")


def rewrite_file():

    confirm = input(
        "\nAre you sure you want to replace all contents? (yes/no): ") .lower()

    if confirm == "yes":
        print("\nEnter the new contents of the file.")
        print("Type 'DONE' on a new line to finish.\n")

        new_content = []

        while True:
            line = input()

            if line.upper() == "DONE":
                break

            new_content.append(line)

        with open("dreams.txt", "w") as file:
            for line in new_content:
                file.write(line + "\n")

        print("\nFile rewritten successfully!\n")

    else:
        print("\nRewrite operation cancelled.\n")

while True:
    print("===== DREAMS FILE MANAGER =====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        read_messages()

    elif choice == "2":
        add_message()

    elif choice == "3":
        rewrite_file()

    elif choice == "4":
        print("\nThank you for using the Dreams File Manager!")
        break

    else:
        print("\nInvalid choice. Please try again.\n")
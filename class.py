import json

borrowed_book = {}


class BookKeeping:
    def __init__(self):
        print("Welcome to the Book Lending System")
        print("-----------------------------------------------")
        options = ("1. View Available Books" "\n"
                   "2. Borrow a Book" "\n"
                   "3. Return a Book" "\n"
                   "4. View Borrowed Books" "\n"
                   "5. Exit")
        print(options)
        # read books_available.json file
        with open("books_avail.json", "r") as file:
            self.available = json.load(file)

        # read borrowed_book.json file
        with open("borrowed_book.json", "r") as f:
            self.borrowed = json.load(f)

        self.n = 0
        print("-----------------------------------------------")
        while True:
            try:
                self.choice = int(input("Choose an option by number: "))
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a number.")

        print("-----------------------------------------------")

        self.user_choice()

    def user_choice(self):

        if self.choice == 1:
            self.view_available_books()

        elif self.choice == 2:
            self.borrow_book()

        elif self.choice == 3:
            self.return_book()

        elif self.choice == 4:
            self.view_borrowed_book()

        elif self.choice == 5:
            self.close()

        else:
            print("You never selected a valid options")
            self.choice = int(input("Choose an option by number : "))

    def view_available_books(self):

        printed_once = False

        for key, value in self.available.items():
            self.n += 1
            if self.n > 0:
                if not printed_once:
                    print("--- Available Books --- ")
                    printed_once = True
                print(f"{self.n}. {key} (Quantity: {value})")
        print("-----------------------------------------------")
        decision = input("Do you want to borrow ? Yes/NO :").lower()
        if decision == "yes":
            print("-----------------------------------------------")
            self.borrow_book()
        elif decision == "no":
            BookKeeping()

    def borrow_book(self):

        printed_once = False
        self.n = 0  # Reset self.n before listing books
        for key, value in self.available.items():
            self.n += 1
            if not printed_once:
                print("--- Available Books --- ")
                printed_once = True
            print(f"{self.n}. {key} (Quantity: {value})")
        print()

        while True:
            try:
                book_choice = int(input("Choose an Option: "))
                if 1 <= book_choice <= self.n:
                    # Access the book title based on the user's choice
                    key, value = list(self.available.items())[book_choice - 1]
                else:
                    print("Invalid option. Please choose a valid book number.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            try:
                book_number = int(input(f"Enter the quantity to borrow (Available: {value}): "))
                if book_number <= 0:
                    print("Please enter a positive number.")
                    continue
                if book_number > value:
                    print("Not enough quantity. Please enter a valid amount.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue

            # Reduce the available quantity
            self.available[key] -= book_number

            # Update the borrowed_book dictionary with details
            borrowed_book[key] = {"quantity": book_number, "borrower": name}
            print(f"\nYou have borrowed '{key}'. Please return it on time.")

            # Write updated data to files
            with open("books_avail.json", "w") as f:
                json.dump(self.available, f, indent=4)

            self.borrowed.update(borrowed_book)
            with open("borrowed_book.json", "w") as f:
                json.dump(self.borrowed, f, indent=4)

            break  # Exit the loop once the book is successfully borrowed

    def return_book(self):
        print("---Borrowed Books--")
        # found = False

        for key, value in self.borrowed.items():
            print(f"{value['quantity']}. {key} - borrowed by {value['borrower']}")

            print("-----------------------------------------------")
            # name_borrower = input("whats your name in the list? :")

            """
                    for key, value in self.borrowed.items():
            
            if name_borrower == value['borrower']:
                # found = True
            """
        book_return = int(input("Enter the book number to return: "))
        print("-----------------------------------------------")

        if book_return > value['quantity']:
            print(f"The number is above what was borrowed by {value['borrower']}")
            book_return = int(input("Enter the book number to return: "))

        elif book_return < value['quantity']:
            print(f"You want to return [{book_return}] you still have [{value['quantity'] - book_return}] "
                  f"more to return")
            confirm = input("do you want to proceed? Yes/No ").lower()
            print("-----------------------------------------------")
            if confirm == "no":
                book_return = int(input("Enter the book number to return: "))
            elif confirm == "yes":
                print()
                print(f"Thank you, {value['borrower']}, for returning '{key}'.")

    def view_borrowed_book(self):

        for key, value in self.borrowed.items():
            print(f"{value['quantity']}. {key} - borrowed by {value['borrower']}")

        print("-----------------------------------------------")
        decision = input("Do you want to borrow ? Yes/NO :").lower()
        if decision == "yes":
            print("-----------------------------------------------")
            self.borrow_book()
        elif decision == "no":
            print("-----------------------------------------------")
            BookKeeping()

    def close(self):
        decision = input("Are you sure you want to Quit ? Yes/NO :").lower()
        if decision == "yes":
            print("-----------------------------------------------")
            print("Good bye")
            exit()
        elif decision == "no":
            print("-----------------------------------------------")
            BookKeeping()


bookkeeping = BookKeeping()

import json

books_avail = {
    'The Great Gatsby': 3,
    'To Kill a Mockingbird': 2,
    '1984': 5,
    'Pride and Prejudice': 4
}

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
        for key, value in books_avail.items():
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
        for key, value in books_avail.items():
            self.n += 1
            if self.n > 0:
                if not printed_once:
                    print("--- Available Books --- ")
                    printed_once = True
                print(f"{self.n}. {key} (Quantity: {value})")
                print()

        while True:
            book_choice = int(input("Choose an Option: "))
            book_number = int(input("Enter the Book Quantity to Borrow: "))
            name = input("Enter your Name: ")
            print()

            # Access the book title based on the user's choice
            key, value = list(books_avail.items())[book_choice - 1]  # Adjust for zero-based index
            print(f"You have selected: {key}")

            # Check if the quantity is available
            if book_number > value:
                print("Not Enough Quantity. Please choose a valid quantity.")
            else:
                # Reduce the available quantity in the library
                books_avail[key] -= book_number
                # Update the borrowed_book dictionary with borrowed details
                borrowed_book[key] = {"quantity": book_number, "borrower": name}
                print(f"You have borrowed {key}. Please return it on time.")
                print(borrowed_book)
                with open("borrowed_book.json", "w") as f:
                    json.dump(borrowed_book, f)
                break  # Exit the loop once the book is successfully borrowed

    def return_book(self):
        print("---Borrowed Books--")
        with open("borrowed_book.json", "r") as f:
            borrowed = json.load(f)

        for key, value in borrowed.items():
            print(f"{value['quantity']}. {key} - borrowed by {value['borrower']}")

        print("-----------------------------------------------")
        book_return = int(input("Enter the book number to return: "))
        print("-----------------------------------------------")
        if book_return > value['quantity']:
            print(f"The number is above what was borrowed by {value['borrower']}")
        elif book_return < value['quantity']:
            print(f"You want to return [{book_return}] you still have [{value['quantity'] - book_return}] "
                  f"more to return")
            confirm = input("do you want to proceed? Yes/No ").lower()
            print("-----------------------------------------------")
            if confirm == "no":
                book_return
            elif confirm == "yes":
                print()
                print(f"Thank you, {value['borrower']}, for returning '{key}'.")

    def view_borrowed_book(self):
        with open("borrowed_book.json", "r") as f:
            borrowed = json.load(f)

        for key, value in borrowed.items():
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

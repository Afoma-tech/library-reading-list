# Names: Afoma Egwuatu, Imaan Ali
# Date: 12th February, 2024
# Title: Group 5 Lab 2
# Description: A program that can store and retrieve information based on the user's reading list

# Import the csv file
import csv

# Define the function to get book data from the user and update reading list
def add_books(title, author, year):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])

# Define the function to display the current reading list
def reading_list():
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")

# Define the function to search for a book in the reading list
def search_book(title):
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        available = False
        for row in reader:
            # An if statement to display the book if available and an error message if not
            if title.lower() in row[0].lower():
                print(f"Title: {row[0]}, Author: {row[1]}")
                available = True

        if not available:
            print("Book not found in reading list")

# Define the function to display the Library Menu
def library_menu():
    while True:
        print("\nLibrary Menu: ")
        print("1. Add a new book")
        print("2. Reading List")
        print("3. Search")
        print("4. Exit Library")

        choice = input("\nEnter your choice: ")
        # An if statement to receive input from the user based on choice
        # If number 1 is chosen, the program will request input from the user.
        if choice == "1":
            title = input("Enter the name of the book: ")
            author = input("Enter the name of the author: ")
            year = input("Enter the publication year: ")
            add_books(title, author, year)

        # If number 2 is chosen, the program will display the user's reading list.
        elif choice == "2":
            reading_list()

        # If number 3 is chosen, the program will request the name of the book to search for.
        elif choice == "3":
            title = input("Enter the name of the book to search: ")
            search_book(title)

        # If number 4 is chosen, the user may exit the eLibrary application.
        elif choice == "4":
            print("Bye Book Lover! Hope to see you soon again the Library.")
            break

        # If neither numbers 1 - 4 are chosen the program will display an error message and restart the loop.
        else:
            print("Invalid option. Please select from numbers 1 to 4.")

# This block of code is to prevent unintended execution and easier testing or debugging.
if __name__ == "__main__":
    library_menu()



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Library:
    def __init__(self):
        self.books = []
        self.issued_books = {}  

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book}' додана до бібліотеки.")

    def remove_book(self, title):
        book_to_remove = next((b for b in self.books if b.title == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Книга '{book_to_remove}' видалена з бібліотеки.")
        else:
            print(f"Книгу '{title}' не знайдено у бібліотеці.")

    def display_books(self):
        if self.books:
            print("Список книг у бібліотеці:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("Бібліотека порожня.")

    def issue_book(self, user, title):
        book_to_issue = next((b for b in self.books if b.title == title), None)
        if book_to_issue and title not in self.issued_books:
            self.issued_books[title] = user
            print(f"Книга '{book_to_issue}' видана користувачу {user}.")
        elif title in self.issued_books:
            print(f"Книга '{title}' вже видана користувачу {self.issued_books[title]}.")
        else:
            print(f"Книгу '{title}' не знайдено в бібліотеці.")

    def return_book(self, title):
        if title in self.issued_books:
            user = self.issued_books.pop(title)
            print(f"Книга '{title}' повернена користувачем {user}.")
        else:
            print(f"Книга '{title}' не видавалася.")

    def display_issued_books(self):
        if self.issued_books:
            print("Список виданих книг:")
            for title, user in self.issued_books.items():
                print(f"- {title} видана {user}")
        else:
            print("Немає виданих книг.")

    def remove_user(self, user_name):
        user_found = False
        for title, user in list(self.issued_books.items()):
            if f"{user.first_name} {user.last_name}" == user_name:
                self.issued_books.pop(title)
                print(f"Книга '{title}' повернена користувачем {user_name}.")
                user_found = True
        if not user_found:
            print(f"Користувача '{user_name}' не знайдено у списку виданих книг.")


def main():
    library = Library()

    while True:
        print("\n1. Додати книгу")
        print("2. Видалити книгу")
        print("3. Показати список книг")
        print("4. Видати книгу користувачу")
        print("5. Повернути книгу")
        print("6. Показати список виданих книг")
        print("7. Видалити користувача з виданих книг")
        print("0. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            title = input("Введіть назву книги: ")
            author = input("Введіть автора книги: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            title = input("Введіть назву книги, яку треба видалити: ")
            library.remove_book(title)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            first_name = input("Введіть ім'я користувача: ")
            last_name = input("Введіть прізвище користувача: ")
            user = User(first_name, last_name)
            title = input("Введіть назву книги, яку хочете видати: ")
            library.issue_book(user, title)

        elif choice == "5":
            title = input("Введіть назву книги, яку повертають: ")
            library.return_book(title)

        elif choice == "6":
            library.display_issued_books()

        elif choice == "7":
            user_name = input("Введіть повне ім'я користувача (Ім'я Прізвище): ")
            library.remove_user(user_name)

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


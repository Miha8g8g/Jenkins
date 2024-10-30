import unittest
from Bib import Library, Book, User

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Ініціалізуємо бібліотеку для кожного тесту"""
        self.library = Library()
        self.book1 = Book("Гаррі Поттер", "Дж.К. Роулінг")
        self.book2 = Book("Властелін кілець", "Дж.Р.Р. Толкін")
        self.user1 = User("Іван", "Іванов")
        self.user2 = User("Петро", "Петров")

    def test_add_book(self):
        """Тест на додавання книги до бібліотеки"""
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)

    def test_remove_book(self):
        """Тест на видалення книги з бібліотеки"""
        self.library.add_book(self.book1)
        self.library.remove_book(self.book1.title)
        self.assertNotIn(self.book1, self.library.books)

    def test_issue_book(self):
        """Тест на видачу книги користувачу"""
        self.library.add_book(self.book1)
        self.library.issue_book(self.user1, self.book1.title)
        self.assertIn(self.book1.title, self.library.issued_books)
        self.assertEqual(self.library.issued_books[self.book1.title], self.user1)
        
    @unittest.expectedFailure
    def test_return_book(self):
        """Тест на повернення книги користувачем (очікувана помилка)"""
        self.library.add_book(self.book1)
        self.library.issue_book(self.user1, self.book1.title)
      # Навмисно викликаємо помилку
        self.library.return_book(self.book1.title)
        self.assertIn(self.book1.title, self.library.issued_books)
        self.assertNotIn(self.book1.title, self.library.issued_books)

        

    def test_display_books(self):
        """Тест на відображення списку книг у бібліотеці"""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.assertEqual(len(self.library.books), 2)

    def test_remove_user(self):
        """Тест на видалення користувача з виданих книг"""
        self.library.add_book(self.book1)
        self.library.issue_book(self.user1, self.book1.title)
        user_full_name = f"{self.user1.first_name} {self.user1.last_name}"
        self.library.remove_user(user_full_name)
        self.assertNotIn(self.book1.title, self.library.issued_books)


if __name__ == '__main__':
    unittest.main()

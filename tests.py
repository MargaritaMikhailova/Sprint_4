import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

   # Проверка 1. Проверить, что новая книга добавилась 
    def test_add_new_book_add_book_in_collector(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и филосовский камень'
    
        collector.add_new_book(book_name)
    
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''

    # Проверка 2. Проверка книги с возрастным рейтингом отсутствует в списке книг для детей 

    def test_get_books_for_children_is_absent_genre_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Медвежонок Паддингтон')  
        collector.add_new_book('Сияние')  

        collector.set_book_genre('Медвежонок Паддингтон', 'Мультфильмы')
        collector.set_book_genre('Сияние', 'Ужасы')

        result = collector.get_books_for_children()
    
        assert 'Ужасы' not in result
        assert 'Детектив' not in result
        assert 'Мультфильмы' in result
        assert len(result) == 1
           
    # Проверка 3. Проверить, что книги с длиной 40 символов не попадают в словарь 

    def test_add_new_book_not_added_if_symbols_more40(self):
        collector = BooksCollector()
        book_name = 'Жареные зеленые помидоры в кафе "Полустанок"'

        collector.add_new_book(book_name)

        assert book_name not in collector.books_genre
    
    # Проверка 4. Проверить, что у добавленной книги нету жанра

    def test_get_book_genre_not_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Десять негритят')

        assert collector.books_genre['Десять негритят'] == ''
        
    # Проверка 5. Проверить, что книги добавляются в Избранном 

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()

        book_name = 'Гарри Поттер и тайная комната'
    
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()
        
    # Проверка 6. Проверить, что книга удаляется из Избранного

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        book_name = 'Мастер и Маргарита'
    
    
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
    
        collector.delete_book_from_favorites(book_name)
    
        assert book_name not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0

    # Проверка 7. Проверить список книг в Избранном

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        book_name = 'Война и мир'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites_list = collector.get_list_of_favorites_books()
        
        assert book_name in favorites_list
        assert len(favorites_list) == 1

    # Проверка 8. Проверить, что жанр книги по её имени отображается 

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()

        book_name = 'Убийства и кексики'
        book_genre = 'Детективы'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        result_genre = collector.get_book_genre(book_name)

        assert result_genre == book_genre
        
    # Проверка 9. Проверить, что получаем словарь books_genre

    @pytest.mark.parametrize('books_with_genres', [
        ({'Понедельник начинается с субботы': 'Фантастика'}),
        ({'ГПонедельник начинается с субботы': 'Фантастика', 'Чиполлино': 'Мультфильмы'}),
        ({})  # Пустой словарь
    ])

    def test_get_books_genre_return_success(self, books_with_genres):
        collector = BooksCollector()

        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        
        result = collector.get_books_genre()
        assert result == books_with_genres
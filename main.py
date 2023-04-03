from database import Database
from Model import BookModel

db = Database(database="Biblioteca", collection="Livros")
db.resetDatabase()

book_model = BookModel(db)

id_book = book_model.create_book("Harry Potter e as Reliquias da Morte", "J.K. Rowling", 2007, 45.5)

book = book_model.read_book_by_id(id_book)

book_model.update_book(id_book, "A Culpa e das Estrelas", "John Green", 2012, 20)

book_model.delete_book(id_book)
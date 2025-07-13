-- mysql.sql
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT NOT NULL,
    publication_year INTEGER NOT NULL,
    genre TEXT NOT NULL,
    format TEXT CHECK(format IN ('p', 'd', 'Physical', 'Digital')) NOT NULL,
    storage_location TEXT NOT NULL
);

INSERT INTO books (title, author, isbn, publication_year, genre, format, storage_location) VALUES
('Waiting for God', 'Simone Weil', '978-0-06-171896-0', 1950, 'Philosophy', 'Digital', 'Shelf 2');

SELECT * FROM books;
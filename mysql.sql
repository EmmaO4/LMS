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

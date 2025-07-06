# script to migrate all csv data into db
import sqlite3
import csv

def migrate_csv_to_db(csv_file="LMS.csv", db_file="db.db", schema_file="mysql.sql"):
    # connect to SQLite DB
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    #load schema
    with open(schema_file, "r") as schema:
        cur.executescript(schema.read())

    # open csv and insert rows
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO books (title, author, isbn, publication_year, genre, format, storage_location)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                row["Title"].strip(),
                row["Author"].strip(),
                row["ISBN"].strip(),
                int(row["Publication Year"]),
                row["Genre"].strip(),
                row["Format"].strip(),
                row["Storage Location"].strip()
            ))

    conn.commit()
    conn.close()
    print(f"Complete: {csv_file} -> {db_file}")

migrate_csv_to_db()

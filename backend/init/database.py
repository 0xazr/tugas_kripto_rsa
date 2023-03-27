# from db import *
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="postgres",
    port="7117"
)

# Koneksi ke database PostgreSQL

# Mengatur koneksi ke autocommit mode
conn.autocommit = True

# Membuat objek cursor
cursor = conn.cursor()

# Query untuk membuat database baru
create_db_query = "CREATE DATABASE db_nisn;"

# Menjalankan query untuk membuat database baru
cursor.execute(create_db_query)

# Menutup koneksi ke database
cursor.close()
conn.close()

print("Database berhasil dibuat!")

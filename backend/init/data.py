from faker import Faker
import psycopg2
import random
from rsa import encrypt

public_key = (2465, 7081)

conn = psycopg2.connect(
    host="127.0.0.1",
    database="db_nisn",
    user="postgres",
    password="postgres",
    port="7117"
)

# Membuat objek cursor
cursor = conn.cursor()

# create a Faker object
fake = Faker()

# generate 100 data
for i in range(100):
    print(i)
    # generate random data
    nisn = encrypt(str(random.randint(3500000000, 3599999999)), public_key)
    nama_siswa = encrypt(fake.first_name(), public_key)
    jenis_kelamin = encrypt(random.choice(['male', 'female']), public_key)
    tempat_lahir = encrypt(fake.city(), public_key)
    tanggal_lahir = encrypt(str(fake.date_of_birth(
        minimum_age=18, maximum_age=25)), public_key)
    agama = encrypt(random.choice(
        ['Islam', 'Kristen', 'Protestan', 'Buddha', 'Kong Hu Cu', 'Hindu']), public_key)
    alamat = encrypt(fake.street_address(), public_key)
    nama_ayah = encrypt(fake.first_name_male(), public_key)
    nama_ibu = encrypt(fake.first_name_female(), public_key)
    alamat_ortu = encrypt(fake.street_address(), public_key)
    no_telp_ortu = encrypt(str(random.randint(10**11, 10**12-1)), public_key)

    # create and execute the SQL query
    query = f"INSERT INTO nisn (nisn, nama_siswa, jenis_kelamin, tempat_lahir, tanggal_lahir, agama, alamat, nama_ayah, nama_ibu, alamat_ortu, no_telp_ortu) VALUES (ARRAY{nisn}, ARRAY{nama_siswa}, ARRAY{jenis_kelamin}, ARRAY{tempat_lahir}, ARRAY{tanggal_lahir}, ARRAY{agama}, ARRAY{alamat}, ARRAY{nama_ayah}, ARRAY{nama_ibu}, ARRAY{alamat_ortu}, ARRAY{no_telp_ortu});"
    # print(query)  # optional, print the query for debugging

    # Menjalankan query untuk membuat tabel baru
    cursor.execute(query)
    # Commit perubahan ke database
    conn.commit()


# Menutup koneksi ke database
cursor.close()
conn.close()

print("Data berhasil dimasukkan!")

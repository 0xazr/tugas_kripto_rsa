import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="db_nisn",
    user="postgres",
    password="123456",
    port="7117"
)

# Membuat objek cursor
cursor = conn.cursor()

# Query untuk membuat tabel baru
create_table_query = """
CREATE TABLE nisn (
  nisn INTEGER[] PRIMARY KEY,
  nama_siswa INTEGER[],
  jenis_kelamin INTEGER[],
  tempat_lahir INTEGER[],
  tanggal_lahir INTEGER[],
  agama INTEGER[],
  alamat INTEGER[],
  nama_ayah INTEGER[],
  nama_ibu INTEGER[],
  alamat_ortu INTEGER[],
  no_telp_ortu INTEGER[]
);
"""

# Menjalankan query untuk membuat tabel baru
cursor.execute(create_table_query)

# Commit perubahan ke database
conn.commit()

# Menutup koneksi ke database
cursor.close()
conn.close()

print("Tabel berhasil dibuat!")

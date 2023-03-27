from flask import Flask, request, jsonify
from flask_cors import CORS
from rsa import encrypt, decrypt
import psycopg2
import json

public_key = (2465, 7081)
private_key = (6497, 7081)

app = Flask(__name__)
CORS(app)
# Koneksi ke database PostgreSQL

conn = psycopg2.connect(
    host="127.0.0.1",
    database="db_nisn",
    user="postgres",
    password="postgres",
    port="7117"
)

# Membuat objek cursor
cursor = conn.cursor()

# Route untuk menambahkan data nisn
@app.route('/api/nisn', methods=['PUT'])
def add_nisn():
    try:
        data = request.get_json()
        
        nisn = encrypt(data['nisn'], public_key)
        nama_siswa = encrypt(data['nama_siswa'], public_key)
        jenis_kelamin = encrypt(data['jenis_kelamin'], public_key)
        tempat_lahir = encrypt(data['tempat_lahir'], public_key)
        tanggal_lahir = encrypt(data['tanggal_lahir'], public_key)
        agama = encrypt(data['agama'], public_key)
        alamat = encrypt(data['alamat'], public_key)
        nama_ayah = encrypt(data['nama_ayah'], public_key)
        nama_ibu = encrypt(data['nama_ibu'], public_key)
        alamat_ortu = encrypt(data['alamat_ortu'], public_key)
        no_telp_ortu = encrypt(data['no_telp_ortu'], public_key)

        insert_query = "INSERT INTO nisn (nisn, nama_siswa, jenis_kelamin, tempat_lahir, tanggal_lahir, agama, alamat, nama_ayah, nama_ibu, alamat_ortu, no_telp_ortu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Menjalankan query untuk memasukkan data ke tabel
        cursor.execute(insert_query, (nisn, nama_siswa, jenis_kelamin, tempat_lahir, tanggal_lahir, agama, alamat, nama_ayah, nama_ibu, alamat_ortu, no_telp_ortu))

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil dimasukkan')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menampilkan semua data nisn
@app.route('/api/nisn', methods=['GET'])
def get_nisn():
    try:
        # Query untuk menampilkan semua data nisn
        select_query = "SELECT * FROM nisn"

        # Menjalankan query untuk menampilkan semua data nisn
        cursor.execute(select_query)

        # Mengambil semua hasil query
        result = cursor.fetchall()

        data = []
        for row in result:
            data.append({
                'nisn': decrypt(row[0], private_key),
                'nama_siswa': decrypt(row[1], private_key),
                'jenis_kelamin': decrypt(row[2], private_key),
                'tempat_lahir': decrypt(row[3], private_key),
                'tanggal_lahir': decrypt(row[4], private_key),
                'agama': decrypt(row[5], private_key),
                'alamat': decrypt(row[6], private_key),
                'nama_ayah': decrypt(row[7], private_key),
                'nama_ibu': decrypt(row[8], private_key),
                'alamat_ortu': decrypt(row[9], private_key),
                'no_telp_ortu': decrypt(row[10], private_key)
            })

        # Menampilkan hasil query
        return jsonify(status=200, message='Data berhasil didapatkan', data=data)
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')
    
# Route untuk menampilkan data nisn berdasarkan nisn
@app.route('/api/nisn/', methods=['POST'])
def get_nisn_by_nisn():
    try:
        data = request.get_json()

        nisn = encrypt(data['nisn'], public_key)
        nama_ibu = encrypt(data['nama_ibu'], public_key)

        # Query untuk menampilkan data nisn berdasarkan nisn
        select_query = "SELECT * FROM nisn WHERE nisn = array%s AND nama_ibu = array%s" % (nisn, nama_ibu)

        # Menjalankan query untuk menampilkan data nisn berdasarkan nisn
        cursor.execute(select_query)

        # Mengambil semua hasil query
        result = cursor.fetchall()
        
        data = []
        for row in result:
            data.append({
                'nisn': decrypt(row[0], private_key),
                'nama_siswa': decrypt(row[1], private_key),
                'jenis_kelamin': decrypt(row[2], private_key),
                'tempat_lahir': decrypt(row[3], private_key),
                'tanggal_lahir': decrypt(row[4], private_key),
                'agama': decrypt(row[5], private_key),
                'alamat': decrypt(row[6], private_key),
                'nama_ayah': decrypt(row[7], private_key),
                'nama_ibu': decrypt(row[8], private_key),
                'alamat_ortu': decrypt(row[9], private_key),
                'no_telp_ortu': decrypt(row[10], private_key)
            })

        # Menampilkan hasil query
        return jsonify(status=200, message='Data berhasil didapatkan', data=data)
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
from rsa import encrypt, decrypt
from flask_session import Session
import psycopg2
import psycopg2.extras
import json
import os
import uuid

UPLOAD_FOLDER = '/mnt/d/Code/rsa-db/backend/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

public_key = (2465, 7081)
private_key = (6497, 7081)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Session(app)

psycopg2.extras.register_uuid()
# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="db_joinevent",
    user="postgres",
    password="postgres",
    port="7117"
)

# Membuat objek cursor
cursor = conn.cursor()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route untuk menambahkan admin
@app.route('/api/admin', methods=['PUT'])
def add_admin():
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Mengambil data dari form
        data = request.get_json()
        
        username = encrypt(data['username'], public_key)
        password = encrypt(data['password'], public_key)

        # Query untuk memasukkan data ke tabel
        insert_query = "INSERT INTO admin (username, password) VALUES (%s, %s)"

        # Menjalankan query untuk memasukkan data ke tabel
        cursor.execute(insert_query, (username, password))

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil dimasukkan')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk login admin
@app.route('/api/admin', methods=['POST'])
def login_admin():
    try:
        # Mengambil data dari form
        data = request.get_json()
        
        username = encrypt(data['username'], public_key)
        password = encrypt(data['password'], public_key)

        # Query untuk mendapatkan data dari tabel
        select_query = "SELECT * FROM admin WHERE username = array%s AND password = array%s" % (username, password)

        # Menjalankan query untuk mendapatkan data dari tabel
        cursor.execute(select_query)

        # Mendapatkan data dari hasil query
        json_data = cursor.fetchall()

        if (json_data == []):
            return jsonify(status=404, message='Failed')
        else:
            # add session
            session['username'] = data['username']
            return jsonify(status=200, message='Success')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk pendataan peserta
@app.route('/api/participant', methods=['POST'])
def add_data():
    try:
        # Mengambil data dari form
        data = request.get_json()
        
        event = data['event']
        name = encrypt(data['name'], public_key)
        email = encrypt(data['email'], public_key)
        phone = encrypt(data['phone'], public_key)
        address = encrypt(data['address'], public_key)
        city = encrypt(data['city'], public_key)
        province = encrypt(data['province'], public_key)
        country = encrypt(data['country'], public_key)
        zip_code = encrypt(data['zip_code'], public_key)
        status = encrypt("0", public_key)

        # Query untuk memasukkan data ke tabel
        insert_query = "INSERT INTO participant (event_id, name, email, phone, address, city, province, country, zip_code, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING participant_id"

        # Menjalankan query untuk memasukkan data ke tabel
        cursor.execute(insert_query, (event, name, email, phone, address, city, province, country, zip_code, status))

        participant = cursor.fetchone()[0]
        
        payment_id = uuid.uuid4().hex

        insert_query = "INSERT INTO payment (payment_id, participant_id, event_id) VALUES (%s, %s, %s)"

        cursor.execute(insert_query, (encrypt(payment_id, public_key), participant, event))

        # Commit perubahan ke database
        conn.commit()
        
        # Menampilkan pesan sukses
        return jsonify(status=200, message={'payment_id': payment_id})
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk upload bukti pembayaran
@app.route('/api/payment/<payment_id>', methods=['POST'])
def upload_payment(payment_id):
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        if 'receipt' not in request.files:
            return jsonify(status=400, message='No file part')
        
        receipt = request.files['receipt']

        if receipt.filename == '':
            return jsonify(status=400, message='No selected file')
        
        filename = uuid.uuid4().hex
        if receipt and allowed_file(receipt.filename):
            filename = secure_filename(filename + '.' + receipt.filename.rsplit('.', 1)[1].lower())
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            receipt.save(file_path)
        
        # Query untuk memasukkan data ke tabel
        insert_query = "INSERT INTO receipt (payment_id, file_path) VALUES (array%s, array%s)" % (encrypt(payment_id, public_key), encrypt(file_path, public_key))

        cursor.execute(insert_query)

        # Commit perubahan ke database
        conn.commit()

        return jsonify(status=200, message='Data berhasil dimasukkan')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menambahkan data pembayaran dan mengubah status peserta
@app.route('/api/payment/<payment_id>', methods=['PUT'])
def add_payment(payment_id):
    # try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Mengambil data dari form
        data = request.get_json()
        
        payment_id = encrypt(payment_id, public_key)
        bank = encrypt(data['bank'], public_key)
        account_number = encrypt(data['account_number'], public_key)

        # Query untuk update data payment
        update_query = "UPDATE payment SET bank = array%s, account_number = array%s WHERE payment_id = array%s" % (bank, account_number, payment_id)

        # Menjalankan query
        cursor.execute(update_query)

        # Query untuk mendapatkan data dari tabel
        select_query = "SELECT participant_id FROM payment WHERE payment_id = array%s" % (payment_id)
        # print(cursor.query)

        cursor.execute(select_query)

        participant = cursor.fetchone()[0]
        
        # Query untuk memasukkan data ke tabel
        update_query = "UPDATE participant SET status = array%s WHERE participant_id = %s" % (encrypt("1", public_key), participant)

        # Menjalankan query untuk memasukkan data ke tabel
        cursor.execute(update_query)

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil dimasukkan')
    # except Exception as e:
        # print(e)
        # return jsonify(status=500, message='Internal server error')

# Route untuk menampilkan data peserta pada event tertentu
@app.route('/api/participant/<event_id>', methods=['GET'])
def get_data(event_id):
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Query untuk mendapatkan data dari tabel
        select_query = "SELECT * FROM participant WHERE event_id = %s"

        # Menjalankan query untuk mendapatkan data dari tabel
        cursor.execute(select_query, (event_id))

        # Mendapatkan data dari hasil query
        json_data = cursor.fetchall()
        
        print(json_data)
        data = []
        for i in range(len(json_data)):
            data.append({
                'id': json_data[i][0],
                'name': decrypt(json_data[i][2], private_key),
                'email': decrypt(json_data[i][3], private_key),
                'phone': decrypt(json_data[i][4], private_key),
                'address': decrypt(json_data[i][5], private_key),
                'city': decrypt(json_data[i][6], private_key),
                'province': decrypt(json_data[i][7], private_key),
                'country': decrypt(json_data[i][8], private_key),
                'zip_code': decrypt(json_data[i][9], private_key)
            })

        # Menampilkan data dalam bentuk JSON
        return jsonify(status=200, data=data)
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menambahkan data event
@app.route('/api/event', methods=['POST'])
def add_event():
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Mengambil data dari form
        data = request.get_json()
        
        name = data['name']
        description = data['description']
        location = data['location']
        date = data['date']
        time = data['time']
        quota = data['quota']
        fee = data['fee']
        
        # Query untuk memasukkan data ke tabel
        insert_query = "INSERT INTO event (name, description, location, date, time, quota, fee) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # Menjalankan query untuk memasukkan data ke tabel
        cursor.execute(insert_query, (name, description, location, date, time, quota, fee))

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil dimasukkan')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menampilkan data event
@app.route('/api/event', methods=['GET'])
def get_event():
    try:
        # Query untuk mendapatkan data dari tabel
        select_query = "SELECT * FROM event"

        # Menjalankan query untuk mendapatkan data dari tabel
        cursor.execute(select_query)

        # Mendapatkan data dari hasil query
        json_data = cursor.fetchall()

        data = []
        for i in range(len(json_data)):
            data.append({
                'id': json_data[i][0],
                'name': json_data[i][1],
                'description': json_data[i][2],
                'location': json_data[i][3],
                'date': json_data[i][4].strftime('%Y-%m-%d'),
                'time': json_data[i][5].strftime('%H:%M:%S'),
                'quota': json_data[i][6],
                'fee': json_data[i][7]
            })

        # Menampilkan data dalam bentuk JSON
        return jsonify(status=200, data=data)
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menampilkan data event berdasarkan id
@app.route('/api/event/<event_id>', methods=['GET'])
def get_event_by_id(event_id):
    try:
        # Query untuk mendapatkan data dari tabel
        select_query = "SELECT * FROM event WHERE event_id = %s" % event_id

        # Menjalankan query untuk mendapatkan data dari tabel
        cursor.execute(select_query)

        # Mendapatkan data dari hasil query
        json_data = cursor.fetchall()
        
        data = []
        for i in range(len(json_data)):
            data.append({
                'id': json_data[i][0],
                'name': json_data[i][1],
                'description': json_data[i][2],
                'location': json_data[i][3],
                'date': json_data[i][4].strftime('%Y-%m-%d'),
                'time': json_data[i][5].strftime('%H:%M:%S'),
                'quota': json_data[i][6],
                'fee': json_data[i][7]
            })

        # Menampilkan data dalam bentuk JSON
        return jsonify(status=200, data=data)
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

# Route untuk menghapus data event berdasarkan id
@app.route('/api/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Query untuk menghapus data dari tabel
        delete_query = "DELETE FROM event WHERE event_id = %s" % event_id

        # Menjalankan query untuk menghapus data dari tabel
        cursor.execute(delete_query)

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil dihapus')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')
    
# Route untuk mengubah data event berdasarkan id
@app.route('/api/event/<event_id>', methods=['PATCH'])
def update_event(event_id):
    try:
        if not session.get('username'):
            return jsonify(status=401, message='Unauthorized')
        
        # Mengambil data dari form
        data = request.get_json()
        
        name = data['name']
        description = data['description']
        location = data['location']
        date = data['date']
        time = data['time']
        quota = data['quota']
        fee = data['fee']
        
        # Query untuk mengubah data dari tabel
        update_query = "UPDATE event SET name = %s, description = %s, location = %s, date = %s, time = %s, quota = %s, fee = %s WHERE event_id = %s"

        # Menjalankan query untuk mengubah data dari tabel
        cursor.execute(update_query, (name, description, location, date, time, quota, fee, event_id))

        # Commit perubahan ke database
        conn.commit()

        # Menampilkan pesan sukses
        return jsonify(status=200, message='Data berhasil diubah')
    except Exception as e:
        print(e)
        return jsonify(status=500, message='Internal server error')

if __name__ == '__main__':
    app.run(debug=True)
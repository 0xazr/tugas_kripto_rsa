import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="db_joinevent",
    user="postgres",
    password="postgres",
    port="7117"
)

# Membuat objek cursor
cursor = conn.cursor()

# Query untuk membuat tabel baru
create_table_query = """
CREATE TABLE admin (
  admin_id SERIAL PRIMARY KEY,
  username INTEGER[],
  password INTEGER[]
);

CREATE TABLE event (
  event_id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  location VARCHAR(255),
  date DATE,
  time TIME,
  quota INT,
  fee DECIMAL(10,2)
);

CREATE TABLE participant (
  participant_id SERIAL PRIMARY KEY,
  event_id INTEGER,
  name INTEGER[],
  email INTEGER[],
  phone INTEGER[],
  address INTEGER[],
  city INTEGER[],
  province INTEGER[],
  country INTEGER[],
  zip_code INTEGER[],
  status INTEGER[],
  FOREIGN KEY (event_id) REFERENCES event(event_id)
);

CREATE TABLE payment (
  payment_id INTEGER[] PRIMARY KEY,
  participant_id INTEGER,
  event_id INTEGER,
  bank INTEGER[],
  account_number INTEGER[],
  FOREIGN KEY (participant_id) REFERENCES participant(participant_id),
  FOREIGN KEY (event_id) REFERENCES event(event_id)
);

CREATE TABLE receipt (
  receipt_id SERIAL PRIMARY KEY,
  payment_id INTEGER[],
  file_path INTEGER[],
  FOREIGN KEY (payment_id) REFERENCES payment(payment_id)
);

INSERT INTO admin (username, password) VALUES ('{6208,3093,4086,4761,4382}', '{6208,3093,4086,4761,4382}'); /** admin:admin **/
INSERT INTO event (name, description, location, date, time, quota, fee) VALUES ('Google Devfest 2022', 'Jakarta', 'Location for event 1', '2021-01-01', '09:00:00', 1000, 0);
"""

# Menjalankan query untuk membuat tabel baru
cursor.execute(create_table_query)

# Commit perubahan ke database
conn.commit()

# Menutup koneksi ke database
cursor.close()
conn.close()

print("Tabel berhasil dibuat!")

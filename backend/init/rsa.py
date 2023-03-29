import random


# Fungsi untuk menentukan apakah sebuah bilangan merupakan bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Fungsi untuk menghasilkan bilangan prima secara acak
def generate_prime():
    prime = random.randint(2, 100)
    while not is_prime(prime):
        prime = random.randint(2, 100)
    return prime


# Fungsi untuk menentukan nilai gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Fungsi untuk menentukan nilai invers modulo
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Fungsi untuk menghasilkan kunci publik dan kunci privat
def generate_keypair():
    # Menghasilkan bilangan prima p dan q secara acak
    p = generate_prime()
    q = generate_prime()

    # Menghitung nilai n dan phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Memilih bilangan bulat e yang relatif prima dengan phi(n)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Menentukan nilai d sebagai invers modulo dari e modulo phi(n)
    d = mod_inverse(e, phi)

    # Mengembalikan kunci publik dan kunci privat
    return ((e, n), (d, n))


# Fungsi untuk mengenkripsi pesan
def encrypt(msg, public_key):
    # Mendeklarasikan variabel-variabel yang diperlukan
    e, n = public_key
    encrypted = []

    # Melakukan enkripsi pada setiap karakter pesan
    for char in msg:
        # Mengubah karakter menjadi bilangan bulat menggunakan kode ASCII
        m = ord(char)

        # Menghitung nilai c = m^e mod n
        c = pow(m, e, n)

        # Menambahkan hasil enkripsi ke dalam daftar encrypted
        encrypted.append(c)

    # Mengembalikan daftar bilangan bulat yang merupakan hasil enkripsi
    return encrypted


# Fungsi untuk mendekripsi pesan
def decrypt(encrypted_msg, private_key):
    # Mendeklarasikan variabel-variabel yang diperlukan
    d, n = private_key
    decrypted = ""

    # Melakukan dekripsi pada setiap bilangan bulat pesan yang telah dienkripsi
    for num in encrypted_msg:
        # Menghitung nilai m = c^d mod n
        m = pow(num, d, n)

        # Mengubah bilangan bulat menjadi karakter menggunakan kode ASCII
        char = chr(m)

        # Menambahkan hasil dekripsi ke dalam variabel decrypted
        decrypted += char

    # Mengembalikan pesan yang telah didekripsi
    return decrypted


# Contoh penggunaan algoritma RSA
if __name__ == "__main__":
    # Menghasilkan kunci publik dan kunci privat
    # public_key, private_key = generate_keypair()

    # print("public: ", public_key)
    # print("private: ", private_key)
    public_key = (2465, 7081)
    private_key = (6497, 7081)

    # Pesan yang akan dienkripsi
    message = "niar@gmail.com"

    # Melakukan enkripsi pesan menggunakan kunci publik
    encrypted_msg = encrypt(message, public_key)

    # Menampilkan pesan yang telah dienkripsi
    print("Encrypted message:", encrypted_msg)

    # Melakukan dekripsi pesan menggunakan kunci privat
    decrypted_msg = decrypt(encrypted_msg, private_key)

    # Menampilkan pesan yang telah didekripsi
    print("Decrypted message:", decrypted_msg)

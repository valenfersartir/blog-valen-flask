#mengimport aplikasi flask untuk web
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur uri
@app.route('/')# ketika alamat ini dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): #function dengan nama hello
    return 'Hello, World!'

#mengatur URI ke http://.../login, dan mengeksekusi fungsi login() jika diakses di
#alamat URI http://.../login
@app.route("/login")
def login():
    return 'halaman login'
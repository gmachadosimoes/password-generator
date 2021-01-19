from flask import Flask, request, render_template, url_for
import string
import secrets

app = Flask(__name__)

@app.route('/')
def index():
    password = ''
    if request.method == 'GET':
        password = pwd_gen()
    return render_template("index.html", password=password)

def pwd_gen():
    alphabet = string.ascii_letters + string.punctuation + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any((c in string.punctuation) for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password

if __name__ == "__main__":
    app.run(debug=False)
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: Select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_digits = 'digits' in request.form
        use_special = 'special' in request.form

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)

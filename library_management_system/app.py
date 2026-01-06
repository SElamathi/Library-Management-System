from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']

        # Dummy credentials check
        if role == 'Admin' and email == 'admin@example.com' and password == 'admin123':
            message = "Welcome, Admin!"
        elif role == 'Member' and email == 'member@example.com' and password == 'member123':
            message = "Welcome, Member!"
        else:
            message = "Invalid credentials or role"

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

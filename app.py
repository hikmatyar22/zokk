from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return render_template('success.html', welcome_message="Welcome", username=name)


if __name__ == '__main__':
    app.run(debug=True)

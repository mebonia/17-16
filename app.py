from flask import Flask, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'  # ან app.secret_key="Python"


@app.route('/')
def home():
    return render_template('home.html')
@app.route("/user")
def user():
    if 'username' in session and len(session['username']) > 0:
        user = session['username']
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session['username'] = request.form["username"]
        return redirect(url_for('user'))

    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template('logout.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        return render_template('search.html', search_query=search_query)

    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)

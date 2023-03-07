from flask import Flask, render_template

app = Flask(__name__)

menu = [{"name":"Наши работы","url": "our_works"},
        {"name": "О нас", "url":"about_us"},
        {"name": "Обратна связь", "url":"call_us"}]

@app.route("/")
def index_page():
    return render_template('index.html', menu=menu)

@app.route("/about/")
def about_page():
    return render_template('about.html', title="О Сайте", menu=menu)

@app.route("/main/")
def main_page():
    return "main"

@app.route("/login/")
def login_page():
    return "login"

@app.route("/stats/")
def stats_page():
    return "stats"

if __name__ == '__main__':
    app.run(debug=True)
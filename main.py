from flask import Flask,render_template

app = Flask(__name__)

# Página de inicio
@app.route("/")
def index():
    return render_template('dash.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
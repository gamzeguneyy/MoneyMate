from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba, MoneyMate'e hoş geldiniiiiz!"

if __name__ == '__main__':
    app.run(debug=True)



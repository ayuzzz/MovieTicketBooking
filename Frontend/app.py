from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def defaultroute():
    try:
        return "Connection to MTB app successful !!"
    except Exception as ex:
        return ex


@app.route('/home')
def homepage():
    return render_template("index.html")


@app.route('/myProfile')
def profile():
    return render_template("profile.html")


@app.route('/myWallet')
def wallet():
    return render_template("wallet.html")


@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html")


if __name__ == '__main__':
    app.run(debug=True)

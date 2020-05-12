from flask import Flask, render_template, jsonify, request
from appsettings import Config
import requests

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


@app.route('/myTransactions')
def transactions():
    return render_template("transactions.html")


@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html")


@app.route('/movies')
def movies():
    try:
        response = requests.get(Config.getAllMoviesUrl)
        response.raise_for_status()
        return render_template("movies.html", movieList=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/movieDetails/<int:movieid>')
def movieDetails(movieid):
    try:
        response = requests.get(Config.getMovieDetailsUrl.format(movieid))
        response.raise_for_status()
        return render_template("movieDetails.html", movieDetails=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/bookTickets/<int:movieid>')
def movieBookingDetails(movieid):
    try:
        response = requests.get(Config.getMovieBookingDetails.format(movieid))
        response.raise_for_status()
        return render_template("bookTickets.html", movieBookingDetails=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/slots')
def slots():
    try:
        response = requests.get(Config.getNonLiveMoviesUrl)
        response.raise_for_status()
        return render_template("slots.html", movieList=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/slotDetails/<int:movieid>')
def slotDetails(movieid):
    try:
        response = requests.get(Config.getMovieDetailsUrl.format(movieid))
        response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(movieid))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/insertSlots', methods=['POST'])
def insertSlots():
    try:
        slotArray = request.get_json(force=True)
        response = requests.post(Config.insertSlotsUrl, json=slotArray)
        response.raise_for_status()
        result = response.json()

        movie_response = requests.get(Config.getMovieDetailsUrl.format(slotArray[0].MovieId))
        movie_response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(slotArray[0].MovieId))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=movie_response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/payment/<int:movieid>/<int:slotid>')
def paymentForTicketBooking(movieid, slotid):
    try:
        response = requests.get(Config.getMovieDetailsUrl.format(movieid))
        response.raise_for_status()

        slot_response = requests.get(Config.slotDetailsForSlotIdUrl.format(slotid))
        slot_response.raise_for_status()

        payment_response = requests.get(Config.getPaymentModesForUserUrl)
        payment_response.raise_for_status()
        return render_template("payments.html", movieDetails=response.json(), slotDetails=slot_response.json(),
                               paymentModes=payment_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/submitPayment', methods=['POST'])
def submitPayment():
    numTickets = int(request.form['number-of-tickets'])
    paymentMode = int(request.form['paymentMode'])
    amount = float(request.form['amount'])
    userid = 1

    requestDict = {'numberOfTickets': numTickets, 'paymentMode': paymentMode, "amount": amount, 'userid': userid}
    response = requests.post(Config.completePaymentUrl, json=requestDict)
    response.raise_for_status()
    result = response.json()

    status = True
    message = "Not enough balance in Wallet"
    return render_template("paymentStatus.html", status=status, message=message)


@app.route('/user-details/<int:userid>', methods=['GET'])
def getUserDetails(userid):
    try:
        response = requests.get(Config.getUserDetails.format(userid))
        response.raise_for_status()

        payment_response = requests.get(Config.getPaymentModesForUserUrl)
        payment_response.raise_for_status()

        return render_template("profile.html", userDetails=response.json(), paymentModes=payment_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/user-details/<int:userid>', methods=['POST'])
def submitUserDetails(userid):
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    primaryContact = str(request.form['primarycontactnumber'])
    country = request.form['country']
    city = request.form['city']
    age = int(request.form['age'])
    paymentMode = int(request.form['paymentMode'])
    userid = userid

    requestDict = {'firstName': firstName, 'paymentMode': paymentMode, 'lastName': lastName, 'primaryContact': primaryContact, 'country':country, 'city':city, 'age':age, 'userid':userid}
    response = requests.post(Config.submitUserDetailsUrl, json=requestDict)
    response.raise_for_status()

    return getUserDetails(userid)


if __name__ == '__main__':
    app.run(debug=True)

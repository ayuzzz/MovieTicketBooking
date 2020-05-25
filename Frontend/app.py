from flask import Flask, render_template, jsonify, request, session, g, redirect
from appsettings import Config
import requests

app = Flask(__name__)
app.secret_key = '083b8434-5c70-41ab-82b3-5a23704bcb1b'


@app.route('/')
def defaultroute():
    try:
        return "Connection to MTB app successful !!"
    except Exception as ex:
        return ex


@app.before_request
def before_request():
    if request.endpoint not in ['defaultroute', 'signin', 'homepage', 'usersignin', 'usersignup', 'usersignout', 'static']:
        if 'userid' in session:
            g.userid = session['userid']
            g.firstName = session['firstName']
            g.lastName = session['lastName']
            g.defaultPaymentMode = session['DefaultPaymentMode']
            return None
        else:
            return redirect('/sign-in')
    return None


@app.route('/home')
def homepage():
    try:
        response = requests.get(Config.getTopBookingsUrl)
        response.raise_for_status()

        movie_response = requests.get(Config.getTopMoviesListUrl)
        movie_response.raise_for_status()
        return render_template("index.html", topBookingList=response.json(), topMoviesList=movie_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/sign-in', methods=['GET'])
def signin():
    return render_template('signin.html')


@app.route('/user-sign-in', methods=['POST'])
def usersignin():
    userName = request.form['userName']
    password = request.form['password']
    requestDict = {'userName':userName, 'password':password}
    response = requests.post(Config.validateUserUrl, json=requestDict)
    response.raise_for_status()
    responses = response.json()
    if responses:
        set_session_variables(responses)
        return redirect('/home')
    else:
        return render_template('signin.html')


def set_session_variables(responses):
    session['userid'] = responses[0]['Id']
    session['firstName'] = responses[0]['FirstName']
    session['lastName'] = responses[0]['LastName']
    session['DefaultPaymentMode'] = responses[0]['DefaultPaymentMethod']

    return None


def reset_session_variables():
    if 'userid' in session:
        session.pop('userid', None)
    if 'firstName' in session:
        session.pop('firstName', None)
    if 'lastName' in session:
        session.pop('lastName', None)
    if 'DefaultPaymentMode' in session:
        session.pop('DefaultPaymentMode', None)

    return None


@app.route('/sign-up', methods=['POST'])
def usersignup():
    return None


@app.route('/sign-out', methods=['GET'])
def usersignout():
    reset_session_variables()
    return redirect('/home')


@app.route('/wishlist')
def wishlist():
    try:
        userid = g.userid
        response = requests.get(Config.getWishlistedMoviesForUserUrl.format(userid))
        response.raise_for_status()
        return render_template("wishlist.html", movieList=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


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
        userid = g.userid
        response = requests.get(Config.getMovieDetailsUrl.format(movieid, userid))
        response.raise_for_status()
        return render_template("movieDetails.html", movieDetails=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/bookTickets/<int:movieid>')
def movieBookingDetails(movieid):
    try:
        userid = g.userid
        response = requests.get(Config.getMovieBookingDetails.format(movieid, userid))
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
        userid = g.userid
        response = requests.get(Config.getMovieDetailsUrl.format(movieid, userid))
        response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(movieid))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/insertSlots', methods=['POST'])
def insertSlots():
    try:
        userid = g.userid
        slotArray = request.get_json(force=True)
        response = requests.post(Config.insertSlotsUrl, json=slotArray)
        response.raise_for_status()
        result = response.json()

        movie_response = requests.get(Config.getMovieDetailsUrl.format(slotArray[0].MovieId, userid))
        movie_response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(slotArray[0].MovieId))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=movie_response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/payment/<int:movieid>/<int:slotid>')
def paymentForTicketBooking(movieid, slotid):
    try:
        userid = g.userid
        response = requests.get(Config.getMovieDetailsUrl.format(movieid, userid))
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
    slotId = request.form['slotId']
    userid = g.userid

    requestDict = {'numberOfTickets': numTickets, 'paymentMode': paymentMode, "amount": amount, 'userid': userid,
                   'slotId': slotId}
    response = requests.post(Config.completePaymentUrl, json=requestDict)
    response.raise_for_status()
    result = response.json()

    status = True
    message = "Not enough balance in Wallet"
    return render_template("paymentStatus.html", status=status, message=message)


@app.route('/user-details', methods=['GET'])
def getUserDetails():
    try:
        userid = g.userid
        response = requests.get(Config.getUserDetails.format(userid))
        response.raise_for_status()

        payment_response = requests.get(Config.getPaymentModesForUserUrl)
        payment_response.raise_for_status()

        return render_template("profile.html", userDetails=response.json(), paymentModes=payment_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/user-details', methods=['POST'])
def submitUserDetails():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    primaryContact = str(request.form['primarycontactnumber'])
    country = request.form['country']
    city = request.form['city']
    age = int(request.form['age'])
    paymentMode = int(request.form['paymentMode'])
    userid = g.userid

    requestDict = {'firstName': firstName, 'paymentMode': paymentMode, 'lastName': lastName,
                   'primaryContact': primaryContact, 'country': country, 'city': city, 'age': age, 'userid': userid}
    response = requests.post(Config.submitUserDetailsUrl, json=requestDict)
    response.raise_for_status()

    return getUserDetails(userid)


@app.route('/booking-details', methods=['GET'])
def getBookingDetailsForUser():
    try:
        userid = g.userid
        response = requests.get(Config.getBookingDetailsForUserUrl.format(userid))
        response.raise_for_status()

        wallet_response = requests.get(Config.getWalletDetailsForUserUrl.format(userid))
        wallet_response.raise_for_status()

        return render_template("wallet.html", bookingDetails=response.json(), walletDetails=wallet_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/addToWishlist/<int:movieid>', methods=['GET'])
def addToWishlist(movieid):
    try:
        userid = g.userid
        response = requests.post(Config.addToWishlistUrl.format(movieid, userid))
        response.raise_for_status()

        movie_response = requests.get(Config.getMovieDetailsUrl.format(movieid, userid))
        movie_response.raise_for_status()

        return render_template("movieDetails.html", movieDetails=movie_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


if __name__ == '__main__':
    app.run(debug=True)

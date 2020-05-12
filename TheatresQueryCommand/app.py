from flask import Flask, jsonify, request
from Services.TheatreService import TheatreService

app = Flask(__name__)


@app.route('/getAllTheatreDetails', methods=['GET'])
def allmoviedetails():
    theatreservice = TheatreService()

    return jsonify(theatreservice.getalltheatres())


@app.route('/slotDetailsForSlotid/<int:slotid>', methods=['GET'])
def slotDetailsForId(slotid):
    theatreservice = TheatreService()

    return jsonify(theatreservice.slotDetailsForId(slotid))


@app.route('/insertSlots', methods=['POST'])
def insertSlots():
    slotArray = request.get_json(force=True)
    theatreservice = TheatreService()

    return jsonify(theatreservice.insertSlotDetails(slotArray))


@app.route('/getMovieBookingDetails/<int:movieid>', methods=['GET'])
def getMovieBookingDetails(movieid):
    theatreservice = TheatreService()

    return jsonify(theatreservice.getmoviebookingdetails(movieid))


if __name__ == '__main__':
    app.run()

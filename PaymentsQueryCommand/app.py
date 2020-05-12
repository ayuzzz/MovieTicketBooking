from flask import Flask, jsonify, request

from Services.PaymentsService import PaymentService

app = Flask(__name__)


@app.route('/getPaymentModesForUser', methods=['GET'])
def getPaymentModesForUser():
    paymentService = PaymentService()
    return jsonify(paymentService.getPaymentModesForUser())


@app.route('/completePayment', methods=['POST'])
def completePayment():
    paymentService = PaymentService()

    jsonRequest = request.get_json()
    return jsonify(paymentService.completePaymentActivity(jsonRequest))


if __name__ == '__main__':
    app.run()

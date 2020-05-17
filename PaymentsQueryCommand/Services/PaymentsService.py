from Repository.PaymentsRepository import PaymentRepository


class PaymentService:
    paymentRepository = PaymentRepository()

    def getPaymentModesForUser(self):
        return self.paymentRepository.getPaymentModesForUser()

    def completePaymentActivity(self, jsonRequest):
        return self.paymentRepository.completePaymentActivity(jsonRequest)

    def getBookingDetails(self, userid):
        return self.paymentRepository.getBookingDetails(userid)

    def getWalletDetails(self, userid):
        return self.paymentRepository.getWalletDetails(userid)

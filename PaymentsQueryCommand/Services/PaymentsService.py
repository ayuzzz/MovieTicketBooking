from Repository.PaymentsRepository import PaymentRepository


class PaymentService:
    paymentRepository = PaymentRepository()

    def getPaymentModesForUser(self):
        return self.paymentRepository.getPaymentModesForUser()

    def completePaymentActivity(self, jsonRequest):
        return self.paymentRepository.completePaymentActivity(jsonRequest)

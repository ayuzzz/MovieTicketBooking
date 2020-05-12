class SqlQueries:
    getAllPaymentModesForUser = """
                                Select Id, PaymentType from payments
                                """

    insertPaymentDetails = """
                           insert into transactions values (0, {}, {}, {}, {});
                           """
    updateWalletBalance = """
                          update wallet set currentBalance = IF (currentBalance >= {0}, currentBalance - {0}, currentBalance) where UserId = {1};
                          """
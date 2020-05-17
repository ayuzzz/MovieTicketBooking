class SqlQueries:
    getAllPaymentModesForUser = """
                                Select Id, PaymentType from payments
                                """

    insertPaymentDetails = """
                           insert into transactions values (0, {0}, {1}, {2}, {3}, CURDATE());
                           """
    updateWalletBalance = """
                          update wallet set currentBalance = IF (currentBalance >= {0}, currentBalance - {0}, currentBalance) where UserId = {1};
                          """
    insertBookingDetails = """
                            insert into bookings values (0, {0}, {1}, LAST_INSERT_ID());
                           """
    getBookingDetails = """
                        select b.Id as BookingId, b.UserId, b.SlotId, b.TransactionId, t.Amount, t.TicketCount, t.Date,
                        p.PaymentType as PaymentMethod, m.Title
                        from bookings b inner join transactions t on b.TransactionId = t.Id and b.UserId = t.UserId
                        inner join payments p on p.Id = t.PaymentMethod
                        inner join slots s on s.Id = b.SlotId
                        inner join movies m on m.Id = s.MovieId
                        where b.UserId = {};
                        """
    getWalletDetails = """select * from wallet where UserId = {};"""
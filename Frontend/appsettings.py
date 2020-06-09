class Config:
    getAllMoviesUrl = "http://192.168.99.100:8001/getAllMovieDetails"
    getMovieDetailsUrl = "http://192.168.99.100:8001/getMovieDetails/{0}/{1}"
    getTheatresDetailsUrl = "http://192.168.99.100:8002/getAllTheatreDetails"
    insertSlotsUrl = "http://192.168.99.100:8002/insertSlots"
    getNonLiveMoviesUrl = "http://192.168.99.100:8001/getNonLiveMovies"
    getMovieBookingDetails = "http://192.168.99.100:8002/getMovieBookingDetails/{}"
    getPaymentModesForUserUrl = "http://192.168.99.100:8003/getPaymentModesForUser"
    completePaymentUrl = "http://192.168.99.100:8003/completePayment"
    slotDetailsForSlotIdUrl = "http://192.168.99.100:8002/slotDetailsForSlotid/{}"
    getUserDetails = "http://192.168.99.100:8004/user-details/{}"
    submitUserDetailsUrl = "http://192.168.99.100:8004/user-details"
    getBookingDetailsForUserUrl = "http://192.168.99.100:8003/booking-details/{}"
    getWalletDetailsForUserUrl = "http://192.168.99.100:8003/wallet-details/{}"
    addToWishlistUrl = "http://192.168.99.100:8001/addToWishlist/{0}/{1}"
    getWishlistedMoviesForUserUrl = "http://192.168.99.100:8001/wishlist/{}"
    getTopBookingsUrl = "http://192.168.99.100:8002/top-bookings"
    getTopMoviesListUrl = "http://192.168.99.100:8001/top-movies"
    validateUserUrl = "http://192.168.99.100:8004/validate-user"

cd D:\Python_Projects\MovieTicketBooking\Frontend
docker build -t mtb-frontend .
docker run -dp 5000:5000 mtb-frontend
echo "`n`n---------------------------------------- mtb-frontend up and running---------------------------------------------------`n`n"

cd D:\Python_Projects\MovieTicketBooking\MoviesQueryCommand
docker build -t mtb-movies-query-command .
docker run -dp 8001:8001 mtb-movies-query-command
echo "`n`n---------------------------------- mtb-movies-query-command up and running---------------------------------------------`n`n"

cd D:\Python_Projects\MovieTicketBooking\TheatresQueryCommand
docker build -t mtb-theatres-query-command .
docker run -dp 8002:8002 mtb-theatres-query-command
echo "`n`n--------------------------------- mtb-theatres-query-command up and running--------------------------------------------`n`n"

cd D:\Python_Projects\MovieTicketBooking\PaymentsQueryCommand
docker build -t mtb-payments-query-command .
docker run -dp 8003:8003 mtb-payments-query-command
echo "`n`n--------------------------------- mtb-payments-query-command up and running--------------------------------------------`n`n"

cd D:\Python_Projects\MovieTicketBooking\UserQueryCommand
docker build -t mtb-user-query-command .
docker run -dp 8004:8004 mtb-user-query-command
echo "`n`n----------------------------------- mtb-user-query-command up and running----------------------------------------------`n`n"

docker ps
<h3>Application Overview</h3>

This a Movie Ticket Booking application which completely follows the <b>microservice architecture</b>, i.e, each service is self sustained and has a connection to a common database(MySQL 5.6). The application is built using pythons's Flask Framework and each microservice is containerized using Docker.

<h3>Branch Details</h3>

-> <b>master</b> : It contains the basic web app<br>
-> <b>docker</b> : It contains the dockerized version of app (dockerfiles present inside each microservice directory). I will be attaching the powershell script (<b>docker_containers.ps1</b>) for building and running each container along with the initial database setup script (<b>Basedata-MTB.sql</b>). (docker image details shared in the Readme.md of <b>docker</b> branch)<br>
-> <b>docker-compose</b> : It contains the containerized version of the application, using <b>docker-compose</b>. The docker-compose.yml is present in the project root directory.


<br>
<h3>Docker images for pulling the images (ready-to-run the application)</h3>
<br><b>-> docker pull ayuzzz1995/mtb-frontend</b>
<br><b>-> docker pull ayuzzz1995/mtb-movies-query-command</b>
<br><b>-> docker pull ayuzzz1995/mtb-theatres-query-command</b></b>
<br><b>-> docker pull ayuzzz1995/mtb-payments-query-command</b>
<br><b>-> docker pull ayuzzz1995/mtb-user-query-command</b>


<br>
<h3>Tech stack</h3>

<h4>Frontend</h4>
- HTML
<br>- CSS
<br>- Javascript
<br>- Bootstrap 4
<br>- Jinja2 templating

<h4>Backend</h4>
- Flask Framework
<br>- Docker
<br>- MySQL Server 5.6


<br>
<h3>Components</h3>

The whole application is divided into 4 microservices: <b>User-Query-Command</b>, <b>Payments-Query-Command</b>, <b>Theatres-Query-Command</b>, <b>Movies-Query-Command</b> and another service which is frontend.


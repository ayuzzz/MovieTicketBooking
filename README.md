<h3>Application Overview</h3>

This a Movie Ticket Booking application which completely follows the <b>microservice architecture</b>, i.e, each service is self sustained and has a connection to a common database(MySQL 5.6). The application is built using pythons's Flask Framework and each microservice is containerized using Docker.

<h3>Branch Details</h3>

-> <b>master</b> : It contains the basic web app<br>
-> <b>docker</b> : It contains the dockerized version of app (dockerfiles present inside each microservice directory). I will be attaching the powershell script for building and running each container. (docker image details shared in the Readme.md of <b>docker</b> branch)<br>
-> <b>docker-compose</b> : It contains the containerized version of the application, using <b>docker-compose</b>. The docker-compose.yml is also present in the project root directory.

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


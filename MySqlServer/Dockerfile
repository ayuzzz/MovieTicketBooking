FROM mysql/mysql-server:5.6
COPY . /MySqlServer
EXPOSE 3306
ENV MYSQL_ROOT_PASSWORD=root@123
CMD mysql -uroot -p'root@123' < MySqlServer/Basedata-MTB.sql
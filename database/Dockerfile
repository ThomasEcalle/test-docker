FROM mysql:8.0.3

ENV MYSQL_ROOT_PASSWORD="babar"
ENV MYSQL_DATABASE="mydb"

ADD mySchema.sql /docker-entrypoint-initdb.d

RUN "mysql -u root --password="bagabu" mydb < /docker-entrypoint-initdb.d"
FROM postgres:10.6

COPY init.sql /docker-entrypoint-initdb.d/

CMD ["postgres", "-c", "logging_collector=on", "-c", "log_statement=all", "-c", "log_destination=csvlog", "-c","log_directory=/tmp", "-c", "log_filename=postgresql.log"]


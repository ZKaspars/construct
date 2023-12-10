# Release 1.0 - code fetches a joke from api, loads response as json, asks user to like or dislike the joke
# Release 1.1 - added ability to choose categories and flags, as well as migrations and db connection
# Release 1.7 -  test implementation finished 


! requires MYSQL community full install with MYSQL Server 8.0 for procedures to work

libraries:

- mysql-connector-python
- yaml
- requests
- logging.config
- logging
- os
- datetime
- configparser

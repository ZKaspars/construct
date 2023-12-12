# Release 1.0 - code fetches a joke from api, loads response as json, asks user to like or dislike the joke
# Release 1.1 - added ability to choose categories and flags, as well as migrations and db connection
<<<<<<< HEAD
# Release 1.7 -  test implementation finished 

=======
# Release 1.7 -  test implementation finished. 
izmainas
>>>>>>> exam_hotfix

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

example of jokeapi json reply:<br />
{<br />
    "error": false,<br />
    "category": "Programming", <br />
    "type": "single", <br />
    "joke": "A man is smoking a cigarette and blowing smoke rings into the air. His girlfriend becomes irritated with the smoke and says \"Can't you see the warning on the cigarette pack? Smoking is hazardous to your health!\" to which the man replies, \"I am a programmer.  We don't worry about warnings; we only worry about errors.\"",<br />
    "flags": {<br />
        "nsfw": false,<br />
        "religious": false,<br />
        "political": false, <br />
        "racist": false, <br />
        "sexist": false, <br />
        "explicit": false <br />
    }, <br />
    "id": 38,
    "safe": true,
    "lang": "en"
}

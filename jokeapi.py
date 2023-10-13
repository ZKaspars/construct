import requests
import json
from db import *

api_url = "https://v2.jokeapi.dev/joke/Any"

# Loading logging configuration
with open('./log_migrate_db.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

#Creating logger
logger = logging.getLogger('root')

# Initiating and reading config values
logger.info('Loading configuration from file')

try:
	config = ConfigParser()
	config.read('config.ini')

	mysql_host = config.get('mysql_config', 'mysql_host')
	mysql_db = config.get('mysql_config', 'mysql_db')
	mysql_user = config.get('mysql_config', 'mysql_user')
	mysql_passwd = config.get('mysql_config', 'mysql_pass')

except:
	logger.exception('')
logger.info('DONE')

req = requests.get(api_url)

# check if connection to api exists 
if req.status_code == 200:
    # load response into json
    parsed_json = json.loads(req.text)
    logger.debug(f"received json:{parsed_json}")
    joke_type = parsed_json['type']
    joke_id = parsed_json['id']
    json_flags = parsed_json['flags']

    # handle joke type (two-part joke or one liner)
    joke_txt = ''
    if joke_type == 'twopart':
        joke_txt = f"{parsed_json['setup']} \n {parsed_json['delivery']}"
    else:
        joke_txt = parsed_json['joke']

    # print joke for user
    print(f"Your joke is: \n \n {joke_txt} \n")

    # get flags of joke
    flag_list = []
    for flag,val in json_flags.items():
        if val == True:
            flag_list.append(flag)

    # print joke's flags
    if len(flag_list) > 0:
        print(f"flags on this joke : {flag_list}")
        logger.debug(f"Flags found: {flag_list}")
    else:
        print("This joke does not have any flags")
        logger.debug("No flags found")


    ans = None
    # loop until valid user input
    logger.debug(f"User entered voting")
    while True:
        try:
            # user votes on joke
            print("\n Did you like this joke? \n")
            inp = str(input("Enter your answer (Y for yes, N for no.): ")).lower()
            # only check first letter of input, in case user types yes or no
            if inp.startswith('y') or inp.startswith('n'):
                ans = inp[0]
                break
            else:
                print("Only Y or N answers allowed!!")
                print(f"Your joke was: \n {joke_txt}")
                logger.info(f"User input was invalid: {inp}")
        except ValueError:
            print("Error: Unexpected value entered.")
            logger.warn(f"User has entered unexpected input: {inp}")
            print(f"Your joke was: \n {joke_txt}")
    print(f"answer was {ans}")
    logger.info(f"User input accepted: {inp}")
    
    # when user likes a joke, it is inserted into the DB 
    if ans == 'y':
        try:
            logger.info(f"Inserting joke into db")
            insert_joke_into_db(joke_id,joke_txt,joke_type,flag_list)
        except:
            logger.error(f"Couldn't insert joke into db")
else:
    logger.error(f"Can't connect to API. Status code: {str(req.status_code)}")
    print(f"Problems connecting to API. Status code: {str(req.status_code)}")

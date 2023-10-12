import json
import requests


api_url = "https://v2.jokeapi.dev/joke/Any"

req = requests.get(api_url)

# check if connection to api exists 
if req.status_code == 200:
    # load response into json
    parsed_json = json.loads(req.text)
    print(parsed_json)

    json_flags = parsed_json['flags']

    # handle joke type (two-part joke or one liner)
    joke_txt = ''
    if parsed_json['type'] == 'twopart':
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
        print(f"flags : {flag_list}")
    else:
        print("This joke does not have any flags")


    ans = None
    # loop until valid user input
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
        except ValueError:
            print("Error: Unexpected value entered.")
            print(f"Your joke was: \n {joke_txt}")
    print(f"answer was {ans}")
    # todo: if ans == y, add joke to db
else:
    print(f"Problems connecting to api. Status code: {str(req.status_code)}")

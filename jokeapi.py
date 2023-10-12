import json
import requests



api_url = "https://v2.jokeapi.dev/joke/Any"


req = requests.get(api_url)

if req.status_code == 200:
    parsed_json = json.loads(req.text)
    print(parsed_json)

    json_flags = parsed_json['flags']

    joke_txt = ''
    if parsed_json['type'] == 'twopart':
        joke_txt = f"{parsed_json['setup']} \n {parsed_json['delivery']}"
    else:
        joke_txt = parsed_json['joke']

    print(f"Your joke is: \n \n {joke_txt} \n")

    flag_list = []
    for flag,val in json_flags.items():
        if val == True:
            flag_list.append(flag)

    if len(flag_list) > 0:
        print(f"flags : {flag_list}")
    else:
        print("This joke does not have any flags")

else:
    print(f"Problems connecting to api. Status code: {str(req.status_code)}")
from db import *


api_url = "https://v2.jokeapi.dev/joke/"

categories = ["Programming","Misc","Dark"\
                ,"Pun","Spooky","Christmas","Any"]

flags = ["nsfw","religious","political","racist",\
            "sexist","explicit","None"]

chosen_flags = []

chosen_categories = []


def add_selection(type,choice):
    global chosen_categories
    global chosen_flags
    if type == "c":
        if choice == "Any":
           logger.info("Category choices deleted")
           chosen_categories = []
        else:
            if choice in chosen_categories:
                logger.debug(f"{choice} already in {chosen_categories}")
            else:
                chosen_categories.append(choice)
                logger.debug(f"{choice} added to {chosen_categories}")

    if type == "f":
        if choice == "None":
            logger.info("Flag choices deleted")
            chosen_flags = []
        else:
            if choice in chosen_flags:
                logger.debug(f"{choice} already in {chosen_flags}")
            else:
                chosen_flags.append(choice)
                logger.debug(f"{choice} added to {chosen_flags}")
    

def choice_selector(kind):
    try:
        working_list = []
        full_name = ""
        select_type = ""
        if kind == "c":
            working_list = categories
            full_name = "CATEGORIES" 
            select_type = "INCLUDE"
            logger.info("Selecting category")
        if kind == "f":
            working_list = flags
            select_type = "EXCLUDE"
            full_name = "FLAGS"
            logger.info("Selecting flags")
        else:
            logger.warning(f"Unexpected use of choice_selector() kind string:{kind}, type of kind variable: {type(kind)}")
    except Error as e:
        logging.error(f"Ran into error: {e}")

    while True:
        try:
            answer = ""
            acceptable_answers = [0,1,2,3,4,5,6,"none","any","s"]
            for index, value in enumerate(working_list):
                print("Choice {}: ||{}||".format(index, value), end=" ")

            print(f"\n which {full_name} do you want to {select_type} ?\n")

            print("Press S to stop selection")
            inp = str(input("Your input: ").lower())
            if inp not in acceptable_answers and int(inp) not in acceptable_answers:
                logging.debug(f"{inp} is not in {acceptable_answers}")
                print("invalid input!")
                continue
            if inp == "s":
                logging.debug(f"{inp} stopped the selection")
                break
            if working_list[int(inp)]:
                answer = working_list[int(inp)]
                logging.debug(f"{inp} is in working list:{working_list}")
            if answer == "Any" or answer == "None":
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(type,working_list[int(inp)])
                logging.debug(f"type: adding selection {type} in working list:{working_list}")
                break
            if working_list[int(inp)]:
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(type,working_list[int(inp)])
            else:
                print("invalid input")
                logging.debug(f"{inp} was invalid")
        except Error as e:
            logger.error(f"Error: {e}")

def runSelections():
    global chosen_categories
    global chosen_flags
    choice_selector("c")
    choice_selector("f")
    chosen_categories= sorted(chosen_categories, key=lambda x: categories.index(x))
    chosen_flags = sorted(chosen_flags, key=lambda x: flags.index(x))

    logger.info(f"Flags list:{chosen_flags}, Categories list: {chosen_categories}")

    categories_string = ','.join(chosen_categories)
    flags_string = ','.join(chosen_flags)

    final_url = ""

    if not chosen_categories and not chosen_flags:
        logger.debug("Flags and categories are empty")
        final_url = "https://v2.jokeapi.dev/joke/Any"
    elif not chosen_flags:
        logger.debug(f"No Flags and Categories: {categories_string} received")
        final_url = f"{api_url}{categories_string}"
    else:
        logger.debug(f"Categories: {categories_string}, and Flags: {flags_string} received")
        final_url = f"{api_url}{categories_string}?blacklistFlags={flags_string}"

    logger.info(f"final_url is {final_url}")
    return final_url
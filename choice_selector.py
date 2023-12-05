from db import *

# these lists are used as key when sorting
categories = ["Programming","Misc","Dark"\
                ,"Pun","Spooky","Christmas","Any"]

flags = ["nsfw","religious","political","racist",\
            "sexist","explicit","None"]

# initialize empty lists
chosen_flags = []

chosen_categories = []

# function called only when user choice needs to be added to flags or categories
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
    
# user selects their flags and categories with this function
def choice_selector(kind):
    #initialize the function, set variables according to selection
    try:
        working_list = []
        full_name = ""
        select_type = ""
        if kind == "c":
            print("ccc")
            working_list = categories
            full_name = "CATEGORIES" 
            select_type = "INCLUDE"
            logger.info("Selecting category")
        if kind == "f":
            print("fff")
            working_list = flags
            select_type = "EXCLUDE"
            full_name = "FLAGS"
            logger.info("Selecting flags")
        else:
            logger.warning(f"Unexpected use of choice_selector() kind string:{kind}, type of kind variable: {type(kind)}")
    except Error as e:
        logging.error(f"Ran into error: {e}")

    # loop until user has finished choosing
    while True:
        try:
            answer = ""
            acceptable_answers = ["0","1","2","3","4","5","6","s"]

            # prints possible choices in one line
            for index, value in enumerate(working_list):
                print("Choice {}: ||{}||".format(index, value), end=" ")

            print(f"\n which {full_name} do you want to {select_type} ?\n")

            print("Press S to stop selection")
            inp = str(input("Your input: ").lower())
            if inp not in acceptable_answers:
                logging.debug(f"{inp} is not in {acceptable_answers}")
                print("invalid input!")
                continue
            if inp == "s":
                logging.debug(f"{inp} stopped the selection")
                break
            # load input as answer only if it exists in current list
            if working_list[int(inp)]:
                answer = working_list[int(inp)]
                logging.debug(f"{inp} is in working list:{working_list}")
            #if user chooses any or none, all preferences are deleted from appropriate list
            if answer == "Any" or answer == "None":
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(kind,working_list[int(inp)])
                logging.debug(f"type: adding selection {kind} in working list:{working_list}")
                answer = None
                break
            if working_list[int(inp)]:
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(kind,working_list[int(inp)])
            else:
                print("invalid input")
                logging.debug(f"{inp} was invalid")
        except Error as e:
            logger.error(f"Error: {e}")

def createUrl(categories_string,flags_string):
    api_url = "https://v2.jokeapi.dev/joke/"

    cat_length = len(categories_string)
    flag_length = len(flags_string)

    # url if no selections made
    if cat_length<1 and flag_length<1:
        logger.debug("Flags and categories are empty")
        final_url = "https://v2.jokeapi.dev/joke/Any"
    # url if there are no blacklisted flags but there are categories
    elif flag_length<1:
        logger.debug(f"No Flags, but Categories: {categories_string} received")
        final_url = f"{api_url}{categories_string}"
    # url with only flags
    elif cat_length<1 and flag_length>0:
        logger.debug(f"No Categories, but Flags {flags_string} received")
        final_url = f"https://v2.jokeapi.dev/joke/Any?{flags_string} "
    else:
    # url with categories and blacklisted flags
        logger.debug(f"Categories: {categories_string}, and Flags: {flags_string} received")
        final_url = f"{api_url}{categories_string}?blacklistFlags={flags_string}"

    # return combined url
    return final_url

# this is called to set both category and flags using previous function
def runSelections():
    global chosen_categories
    global chosen_flags
    choice_selector("c")
    choice_selector("f")
    # sort in the correct order, otherwise API will not accept the link
    chosen_categories= sorted(chosen_categories, key=lambda x: categories.index(x))
    chosen_flags = sorted(chosen_flags, key=lambda x: flags.index(x))

    logger.info(f"Flags list:{chosen_flags}, Categories list: {chosen_categories}")
    # convert to a string from list
    categories_string = ','.join(chosen_categories)
    flags_string = ','.join(chosen_flags)

    final_url = createUrl(categories_string,flags_string)

    logger.info(f"final_url is {final_url}")
    # return combined url
    return final_url

def defaultSelections():
    #default blacklist flags: excluding nsfw, racist and sexit jokes
    return "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist"



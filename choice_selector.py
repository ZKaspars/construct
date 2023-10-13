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
    

def choice_selector(type):
    working_list = []
    full_name = ""
    select_type = ""
    if type == "c":
        working_list = categories
        full_name = "categories" 
        select_type = "include"
        logger.info("Selecting category")
    if type == "f":
        working_list = flags
        select_type = "exclude"
        full_name = "flags"
        logger.info("Selecting flags")
    else:
        logger.error("Unexpected use of choice_selector()")

    while True:
        try:
            answer = ""
            acceptable_answers = [0,1,2,3,4,5,6,"none","any","s"]
            for index, value in enumerate(working_list):
                print("Choice {}: ||{}||".format(index, value), end=" ")

            print(f"\n which {full_name} do you want to {select_type} ?\n")

            print("Press S to stop selection")
            inp = str(input("Your input: ").lower())
            if inp not in acceptable_answers:
                print("invalid input!")
                continue
            if inp == "s":
                break
            if working_list[int(inp)]:
                answer = working_list[int(inp)]
            if answer == "Any" or answer == "None":
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(type,working_list[int(inp)])
                break
            if working_list[int(inp)]:
                logging.info(f"{working_list[int(inp)]} selected")
                add_selection(type,working_list[int(inp)])
            else:
                print("invalid input")
        except Error as e:
            logger.error(f"Error: {e}")

def runSelections():
    choice_selector("c")
    choice_selector("f")
    chosen_categories.sort(categories)
    chosen_flags.sort(flags)


choice_selector("c")
choice_selector("f")
print(chosen_flags,chosen_categories)
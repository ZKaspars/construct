from db import *
from choice_selector import *

print("Testing if database insertion is functional\n ")
args = (11, "Why did the chicken cross the road?", "single", ['funny'])
print(f"Insertion args: {args}")
assert insert_joke_into_db(args[0],args[1],args[2],args[3]) == True
print("Database insertion test: Finished \n")


print("Testing if createURL function is returning correct URL\n")

print("Test 1: empty string")
assert createUrl("","") == "https://v2.jokeapi.dev/joke/Any"
print("Test 1 finished \n")

categories = "Programming,Christmas"
blacklist = "nsfw,racist,sexist"
print(f"Test 2: categories: {categories} and blacklist: {blacklist}")
assert createUrl(categories,blacklist) == "https://v2.jokeapi.dev/joke/Programming,Christmas?blacklistFlags=nsfw,racist,sexist"
print("Test 2 finished \n")





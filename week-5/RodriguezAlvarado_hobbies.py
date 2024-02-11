"""
    Title: RodriguezAlvarado_hobbies.py
    Author: Zadkiel Rodriguez Alvarado
    Date: 01/21/2024
    Description: Create lists
    Sources: 
        https://www.w3schools.com/python/python_lists.asp
        https://www.w3schools.com/python/python_lists_loop.asp
"""
# Hobbies list
hobbies_list = ["Video games", "Coding", "Music", "TV", "Puzzles"]

# Loop through the Hobbies list and print them to the console window
for hobby in hobbies_list:
    print(hobby)

# Days list
days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Loop through the days list and print them to the console
# If the day is Saturday or Sunday then print "you are off and should enjoy your hobbies"
# If it is any other day then print "work day"
for day in days_list:
    if(day == "Sunday" or day == "Saturday"):
        print(day + " - You are off today. Go enjoy your hobbies!")
    else:
        print(day + " - Today is a work day!")


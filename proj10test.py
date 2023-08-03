#################################################
# Do not modify this section
# You must place 'monster_mash.json' in the same
# directory as this file.
from cisc108 import assert_equal
import json

with open('monster_mash.json') as data_file:
    MONSTER_MASH = json.load(data_file)

#################################################
# Your code goes below

# ...
# Add more test cases by looking at:
# https://codebeautify.org/online-json-editor/cb58cc0b



Grave = {'name': str, 'Message': str}

'''
G2. Define the function `count_grave_characters` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Do not count spaces and new lines.
'''
def count_grave_characters(graves: [Grave]) -> int:
    '''
    Consumes a list of graves and produces an integer value
    representing the number of characters neeeded to write
    the messages of the graves, but not including spaces and new lines.
    
    Args:
        graves ([Grave]): The list of graves that is given.
    Returns:
        int: The integer value indicating the number of characters needed
            to write all of the messages of the graves.
    '''
    total = 0
    for grave in graves:
        for word in grave["message"].split():
            total = total + len(word)
    return total

assert_equal(count_grave_characters(MONSTER_MASH['graves 2']), 90)
assert_equal(count_grave_characters(MONSTER_MASH['graves 3']), 95)
assert_equal(count_grave_characters(MONSTER_MASH['graves 4']), 0)

'''
G3. Define a function named `estimate_grave_cost` that consumes a list of graves
and produces an integer representing the total estimate lettering cost by
multiplying the number of letters on the grave (ignoring spaces and newlines) by
the cost of writing a letter ($2).
'''
def estimate_grace_cost(graves: [Grave]) -> int:
    '''
    Consumes a list of graves and produces an integer value
    representing the total estimate lettering cost by multiplying
    the number of letters on the grave (ignoring spaces and newlines)
    by $2 (cost to write a letter).
    
    Args:
        graves ([Grave]): The list of graves that is given.
    Returns:
        int: The integer value indicating the total estimate lettering cost.
    '''
    return count_grave_characters(graves) * 2

assert_equal(estimate_grace_cost(MONSTER_MASH['graves 1']), 240)
assert_equal(estimate_grace_cost(MONSTER_MASH['graves 2']), 180)
assert_equal(estimate_grace_cost(MONSTER_MASH['graves 3']), 190)


"""
G4. Define a function named `count_shouters` that consumes a list of graves
and produces an integer representing the number of graves that had their
messages in all capital letters. Hint: use the `.upper()` method.
"""
def count_shouters(graves: [Grave]) -> int:
    '''
    Consumes a list of graves and produces an integer value
    representing the number of graves that has a message that is
    in all capital letters. 
    
    Args:
        graves ([Grave]): The list of graves that is given.
    Returns:
        int: The integer value indicating the number of graves that
        has a message that is in all capital letters. 
    '''
    count = 0
    for grave in graves:
        if grave["message"] == grave["message"].upper():
            count = count + 1
    return count

assert_equal(count_shouters(MONSTER_MASH['graves 1']), 3)
assert_equal(count_shouters(MONSTER_MASH['graves 2']), 1)
assert_equal(count_shouters(MONSTER_MASH['graves 3']), 1)


## Treats

'''
A Treat is a dictionary with the following keys
* "name": A string value indicating the name of the treat
* "chocolate?": A boolean indicating whether the treat involves chocolate
* "calories": An integer representing how many calories are in the treat
* "quantity": An integer indicating the typical serving size of the treat.
'''

Treat = {'name': str, 'chocolate?': bool, 'calories': int, 'quantity': int}



'''
T1. You are going through a series of houses and you get a treat from
each one. Define a function `eat_treats` that consumes a list of treats and
produces the total number of calories in all the treats.
'''
def eat_candy(treats: [Treat]) -> int:
    '''
    Consumes a list of treats and produces an integer value
    representing the total calories of all the treats in the list.
    
    Args:
        treats ([Treat]): The list of treats that is given.
    Returns:
        int: The integer value indicating the total calories in the treats.
    '''
    calories = 0
    for treat in treats:
        calories = calories + treat["calories"]
    return calories

assert_equal(eat_candy(MONSTER_MASH['treats 1']), 563)
assert_equal(eat_candy(MONSTER_MASH['treats 2']), 280)
assert_equal(eat_candy(MONSTER_MASH['treats 3']), 407)


'''
T2. Define a function `find_most_calorific_ratio` that consumes a list
of treats and produces a float representing the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''
def find_most_calorific_ratio(treats: [Treat]) -> float:
    '''
    Consumes a list of treats and produces a float value
    representing the treat with the highest calories per quntity.
    And if list is empty return None.
    
    Args:
        treats ([Treat]): The list of treats that is given.
    Returns:
        float: The float value indicating the highest calories per quntity.
    '''
    if treats:
        highest = 0
        for treat in treats:
            ratio = treat["calories"] / treat["quantity"]
            if highest < ratio:
                highest = ratio
        return highest
    else:
        return None

assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 4']), 214.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 5']), 7.368421052631579)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 6']), None)


'''
T3. Define a function `find_most_calorific` that consumes a list
of treats and produces a string representing the name of the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''
def find_most_calorific(treats: [Treat]) -> str:
    '''
    Consumes a list of treats and produces a string 
    representing the name of the treat with the highest
    calories per quantity. Return None if list empty.
    
    Args:
        treats ([Treat]): The list of treats that is given.
    Returns:
        str: The string indicating the name of the treat with
            the highest calories per quntity.
    '''
    if treats:
        ratio = find_most_calorific_ratio(treats)
        for treat in treats:
            if (treat["calories"] / treat["quantity"]) == ratio:
                mostCalorific = treat["name"]
        return mostCalorific
    else:
        return None

assert_equal(find_most_calorific(MONSTER_MASH['treats 4']), "Candy Apple")
assert_equal(find_most_calorific(MONSTER_MASH['treats 5']), "Candy Corn")
assert_equal(find_most_calorific(MONSTER_MASH['treats 6']), None)


'''
T4. Define a function named `count_chocolates` that consumes a list of treats
and produces the number of treats that are made of chocolate.
'''
def count_chocolates(treats: [Treat]) -> int:
    '''
    Consumes a list of treats and produces an integer value 
    representing the number of treats that are made of chocolate.
    
    Args:
        treats ([Treat]): The list of treats that is given.
    Returns:
        int: The integer value indicating the number of treats
            made of chocolate.
    '''
    count = 0
    for treat in treats:
        if treat["chocolate?"]:
            count = count + 1
    return count

assert_equal(count_chocolates(MONSTER_MASH['treats 1']), 2)
assert_equal(count_chocolates(MONSTER_MASH['treats 2']), 4)
assert_equal(count_chocolates(MONSTER_MASH['treats 3']), 2)


'''
T5. Define a function named `get_choco_quantity` that consumes a list
of treats and produces an integer representing the total quantities
of all the chocolate treats.
'''
def get_choco_quantity(treats: [Treat]) -> int:
    '''
    Consumes a list of treats and produces an integer value 
    representing the quanity of chocolate treats. 
    
    Args:
        treats ([Treat]): The list of treats that is given.
    Returns:
        int: The integer value indicating the quantity of all
            chocolate treats. 
    '''
    choco = 0
    for treat in treats:
        if treat["chocolate?"]:
            choco = choco + treat["quantity"]
    return choco

assert_equal(get_choco_quantity(MONSTER_MASH['treats 2']), 8)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 3']), 19)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 4']), 0)


## Media

'''
A Media is a dictionary with the following keys:
* "name": The name of this media
* "kind": Either "movie", "song", or "game"
* "duration": The length of this media in minutes
'''

Media = {'name': str, 'kind': str, 'duration': int}


'''
E1. Define a function `total_duration` that consumes a list of Media
and produces their total duration.
'''
def total_duration(medias: [Media]) -> int:
    '''
    Consumes a list of medias and produces an integer value 
    representing the total duration. 
    
    Args:
        medias ([Media]): The list of medias that is given.
    Returns:
        int: The integer value indicating the total duration.
    '''
    total = 0
    for media in medias:
        total = total + media["duration"]
    return total

assert_equal(total_duration(MONSTER_MASH['media 1']), 383)
assert_equal(total_duration(MONSTER_MASH['media 2']), 146)
assert_equal(total_duration(MONSTER_MASH['media 3']), 1440)


'''
E2. Define the function `count_not_long` that consumes a list of media
and produces the number of items that are less than 100 minutes long.
'''
def count_not_long(medias: [Media]) -> int:
    count = 0
    for media in medias:
        if media["duration"] < 100:
            count = count + 1
    return count

assert_equal(count_not_long(MONSTER_MASH['media 2']), 4)
assert_equal(count_not_long(MONSTER_MASH['media 3']), 0)
assert_equal(count_not_long(MONSTER_MASH['media 4']), 2)






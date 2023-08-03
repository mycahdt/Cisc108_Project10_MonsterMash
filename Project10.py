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

## Party
'''
A Party is a dictionary with four fields:
* "type": The type of party that it is
* "werewolves": The number of werewolves in attendance
* "vampires": The number of vampires in attendance
* "witches": The number of witches in attendance
'''

Party = {"werewolves": int, "vampires": int, "witches": int,
         "type": str}


"""
P1. Define a function `sum_guests` that consumes a Party and
produces an integer representing the total number of
guests attending (including werewolves, vampires, and witches).
"""
def sum_guests(party: Party) -> int:
    '''
    Consumes the party dictionary and produces
    an integer that represents the total number
    of werewolves, vampires, and witches that are attending.
    
    Args:
        party (Party): The dictionary that holds the keys of
            'werewolves', 'vampires', 'witches' and their
            corresponding values.
    Returns:
        int: The integer value representing the number of guests
            attending the party which includes the total number
            of werewolves, vampires, and witches.
    '''
    werewolves = party['werewolves']
    vampires = party['vampires']
    witches = party['witches']
    return werewolves + vampires + witches

assert_equal(sum_guests(MONSTER_MASH['party 1']), 20)
assert_equal(sum_guests(MONSTER_MASH['party 2']), 25)
assert_equal(sum_guests(MONSTER_MASH['party 3']), 19)


"""
P2. Define a function `were_only_werewolves` that consumes a Party and
produces a boolean indicating whether or not the only guests were
werewolves.
"""
def were_only_werewolves(party: Party) -> bool:
    '''
    Consumes the party dictionary and produces
    a boolean value that indicates whether or not
    the guests were only werewolves.
    
    Args:
        party (Party): The dictionary that holds the keys of
            'werewolves', 'vampires', 'witches' and their
            corresponding values.
    Returns:
        bool: The boolean value indicating if the guests
            are only werewolves or not. 
    '''
    return party['vampires'] == 0 and party['witches'] == 0

assert_equal(were_only_werewolves(MONSTER_MASH['party 2']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 3']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 4']), True)


'''
P3. Witches and vampires always bring a date, but werewolves prefer to
come to parties alone (because they're lone wolves). Define a function
`total_folks` that consumes a Party and produces an integer representing
the total number of folks who were present.
'''
def total_folks(party: Party) -> int:
    '''
    Consumes the party dictionary and produces
    an integer value representing the total
    numebr of folks, considering that witches
    and vampires bring a date and werewolves
    come alone. 
    
    Args:
        party (Party): The dictionary that holds the keys of
            'werewolves', 'vampires', 'witches' and their
            corresponding values.
    Returns:
        int: The integer value representing the total folks
            that are attending the party. 
    '''
    witches = party['witches'] * 2
    vampires = party['vampires'] * 2
    return party['werewolves'] + witches + vampires

assert_equal(total_folks(MONSTER_MASH['party 3']), 38)
assert_equal(total_folks(MONSTER_MASH['party 4']), 33)
assert_equal(total_folks(MONSTER_MASH['party 5']), 85)


'''
P4. A "small" party has 20 or fewer guests, a "big" party has 40 or more,
and otherwise the party is "medium". Define a function `check_party_size`
that consumes a Party and produces a string indicating whether the party
is "small", "medium", or "big". Note that we're counting guests, not folks,
so don't include witches' and vampires' dates.
'''
def check_party_size(party: Party) -> str:
    '''
    Consumes the party dictionary and produces a string that states
    if the party is small, medium, or big. A small party has 20 or
    less guests, a big party has 40 or more guests, and a medium
    party has between 20 and 40 guests. 
    
    Args:
        party (Party): The dictionary that holds the keys of
            'werewolves', 'vampires', 'witches' and their
            corresponding values.
    Returns:
        str: The string which states if the party is small, medium, or big. 
    '''
    guests = sum_guests(party)
    if guests <= 20:
        return "small"
    elif guests >= 40:
        return "big"
    else:
        return "medium"

assert_equal(check_party_size(MONSTER_MASH['party 4']), "medium")
assert_equal(check_party_size(MONSTER_MASH['party 5']), "big")
assert_equal(check_party_size(MONSTER_MASH['party 1']), "small")


'''
P5. If a party has both werewolves and vampires, there should be
more werewolves than vampires. Define a function `check_party_ratio`
that consumes a Party and produces a float indicating the number of
werewolves divided by the number of vampires. If there are no vampires
or no werewolves, produce the value 0.
'''
def check_party_ratio(party: Party) -> float:
    '''
    Consumes the party dictionary and produces a float value that
    indicates the ratio of werewolves to vampires, which is done
    by taking the number of werewolves divided by number of
    vampires
    
    Args:
        party (Party): The dictionary that holds the keys of
            'werewolves', 'vampires', 'witches' and their
            corresponding values.
    Returns:
        float: The float value indicating the ratio of
            werewolves to vampires. 
    '''
    if party['werewolves'] == 0 or party['vampires'] == 0:
        return 0
    else:
        return party['werewolves'] / party['vampires']

assert_equal(check_party_ratio(MONSTER_MASH['party 5']), 3.0)
assert_equal(check_party_ratio(MONSTER_MASH['party 1']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 2']), 0.25)


## Monsters
'''
A Monster is a dictionary with four fields:
* "name": The name of this particular monster (string)
* "kind": A str representing the type of the monster (e.g., "vampire", "werewolf")
* "spookyiness": An integer from 0-4 indicating its spookiness
* "undead?": A boolean indicating whether or not this monster is undead.
'''

Monster = {"name": str, "kind": str, "spookiness": int, "undead?": bool}


'''
M1. Define a function `count_monsters` that consumes a list of monsters and
produces an integer indicating how many monsters there are.
'''
def count_monsters(monsters: [Monster]) -> int:
    '''
    Consumes a list of monsters and produces an integer
    which represents the total number of monsters. 
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        int: The int value indicating the total monsters. 
    '''
    count = 0
    for monster in monsters:
        count = count + 1
    return count

assert_equal(count_monsters(MONSTER_MASH['monsters 1']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 3']), 5)


'''
M2. Define a function `count_undead_monsters` that consumes a list
of monsters and produces an integer indicating how many undead
monsters there are.
'''
def count_undead_monsters(monsters: [Monster]) -> int:
    '''
    Consumes a list of monsters and produces an integer
    which represents the number of undead monsters. 
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        int: The integer value indicating the number of undead monsters. 
    '''
    undead = 0
    for monster in monsters:
        if monster["undead?"]:
            undead = undead + 1
    return undead

assert_equal(count_undead_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 3']), 2)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 4']), 4)
    
            
'''
M3. Define a function `average_spookiness` that consumes a list of monsters
and produces a float representing their average spookiness. If the list
is empty, produce the special value `None` instead.
'''
def average_spookiness(monsters: [Monster]) -> float:
    '''
    Consumes a list of monsters and produces a float
    which represents the average spookiness. And if the list
    of monsters is empty, it returns None.
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        float: The float value indicating the average spookiness. 
    '''
    if monsters:
        avgSpookiness = 0
        for monster in monsters:
            avgSpookiness = avgSpookiness + monster["spookiness"]
        avgSpookiness = avgSpookiness / count_monsters(monsters)
        return avgSpookiness
    else:
        return None

assert_equal(average_spookiness(MONSTER_MASH['monsters 3']), 1.8)
assert_equal(average_spookiness(MONSTER_MASH['monsters 4']), 1.6)
assert_equal(average_spookiness(MONSTER_MASH['monsters 6']), None)
        

'''
M4. Define a function `average_undead_spookiness` that consumes a list of monsters
and produces a float representing the average spookiness of the undead monsters
in the list. If there are no undead monsters, produce the special value `None`
instead.
'''
def average_undead_spookiness(monsters: [Monster]) -> float:
    '''
    Consumes a list of monsters and produces a float
    which represents the average spookiness of undead monsters.
    And if the list has no undead monsters it returns None.
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        float: The float value indicating the average spookiness
            of undead monsters. 
    '''
    numUndead = count_undead_monsters(monsters)
    if numUndead == 0:
        return None
    else:
        avgSpookiness = 0
        count = 0
        for monster in monsters:
            if monster["undead?"]:
                avgSpookiness = avgSpookiness + monster["spookiness"]
                count = count + 1
        avgSpookiness = avgSpookiness / count
        return avgSpookiness

assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 4']), 2.0)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 5']), 0.66666666)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 1']), None)


'''
M5. Define a function `count_spooky_monsters` that consumes a list of monsters
and produces an integer indicating how many monsters have a spookiness of
2 or more.
'''
def count_spooky_monsters(monsters: [Monster]) -> int:
    '''
    Consumes a list of monsters and produces an integer
    which represents the number of monsters that have
    a spookiness that is 2 or more.
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        int: The integer value indicating the number of monsters
        that have a spookiness that is 2 or more.
    '''
    count = 0
    for monster in monsters:
        if monster["spookiness"] >= 2:
            count = count + 1
    return count

assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 3']), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 4']), 3)


'''
M6. Define the function `count_vampires` that consumes a list of monsters
and produces an integer indicating how many monsters are of the kind
"vampire".
'''
def count_vampires(monsters: [Monster]) -> int:
    '''
    Consumes a list of monsters and produces an integer
    which represents the number of monsters that are the
    kind 'vampire'.
    
    Args:
        monsters ([Monster]): The list of monsters that is given.
    Returns:
        int: The integer value indicating the number of monsters
        that are the kind 'vampire'
    '''
    count = 0
    for monster in monsters:
        if monster["kind"] == "vampire":
            count = count + 1
    return count

assert_equal(count_vampires(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_vampires(MONSTER_MASH['monsters 3']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 5']), 2)
            

## Costumes
'''
A Costume is a dictionary with 3 keys:
* 'label': A string representing the name of the costume.
* 'price': An integer representing the cost of the costume in dollars.
* 'sizes': A list of strings representing the available sizes ('S', 'M', 'L').
'''

Costume = {'label': str, 'price': int, 'sizes': [str]}


'''
C1. Define a function `count_costumes` that consumes a list of costumes
and produces an integer representing the number of costumes in the list.
'''
def count_costumes(costumes: [Costume]) -> int:
    '''
    Consumes a list of costumes and produces an integer
    which represents the total number of costumes. 
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        int: The int value indicating the total costumes. 
    '''
    count = 0
    for costume in costumes:
        count = count + 1
    return count

assert_equal(count_costumes(MONSTER_MASH['costumes 1']), 4)
assert_equal(count_costumes(MONSTER_MASH['costumes 2']), 3)
assert_equal(count_costumes(MONSTER_MASH['costumes 4']), 5)


'''
C2. Define a function `total_price` that consumes a list of costumes
and produces an integer representing the total price of all the
costumes in the list.
'''
def total_price(costumes: [Costume]) -> int:
    '''
    Consumes a list of costumes and produces an integer
    which represents the total price of all the costumes
    in the list. 
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        int: The int value indicating the total price of
            all the costumes in the list.
    '''
    total = 0
    for costume in costumes:
        total = total + costume["price"]
    return total

assert_equal(total_price(MONSTER_MASH['costumes 2']), 105)
assert_equal(total_price(MONSTER_MASH['costumes 3']), 21)
assert_equal(total_price(MONSTER_MASH['costumes 4']), 340)


'''
C3. Define a function `count_sizes` that consumes a list of costumes and
produces an integer indicating the total number of sizes that are
available across all the costumes.
'''
def count_sizes(costumes: [Costume]) -> int:
    '''
    Consumes a list of costumes and produces an integer
    which represents the total number of sizes that are
    available across all the costumes.
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        int: The int value indicating the total number of
            sizes that are available across all the costumes.
    '''
    count = 0
    for costume in costumes:
        for size in costume["sizes"]:
            count = count + 1
    return count

assert_equal(count_sizes(MONSTER_MASH['costumes 3']), 12)
assert_equal(count_sizes(MONSTER_MASH['costumes 4']), 9)
assert_equal(count_sizes(MONSTER_MASH['costumes 5']), 4)


'''
C4. Define a function `max_price` that consumes a list of costumes
and produces an integer indicating the price of the most expensive
costume. If there are no costumes in the list, produce the special
value `None`.
'''
def max_price(costumes: [Costume]) -> int:
    '''
    Consumes a list of costumes and produces an integer
    which represents the price of the most expensive costume.
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        int: The int value indicating the price of
            the most expensive costume.
    '''
    if costumes:
        maximum = 0
        for costume in costumes:
            if costume["price"] > maximum:
                maximum = costume["price"]
        return maximum
    else:
        return None

assert_equal(max_price(MONSTER_MASH['costumes 4']), 80)
assert_equal(max_price(MONSTER_MASH['costumes 5']), 40)
assert_equal(max_price(MONSTER_MASH['costumes 6']), None)


'''
C5. Define a function `most_expensive_costume` that consumes
a list of costumes and produces a string representing the label
of the costume with the highest price. In the event of a tie,
give the label of the item later in the list. If there are no
costumes, return the special value None.
'''
def most_expensive_costume(costumes: [Costume]) -> str:
    '''
    Consumes a list of costumes and produces a string
    which represents label of the costume with the
    highest price. If there are no costumes return None.
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        str: The string indicating the label of the costume
            that has the highest price. 
    '''
    if costumes:
        maxPrice = max_price(costumes)
        expensiveCostume = ""
        for costume in costumes:
            if costume["price"] == maxPrice:
                expensiveCostume = costume["label"]
        return expensiveCostume
    else:
        return None

assert_equal(most_expensive_costume(MONSTER_MASH['costumes 1']), "Pirate Zombie Ghost")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 3']), "Ghost")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 6']), None)


'''
C6. Define a function `find_last_medium` that consumes a list of costumes
and produces the label of the last costume that is available in a medium.
If no medium costumes are found, produce the special value `None`.
'''
def find_last_medium(costumes: [Costume]) -> str:
    '''
    Consumes a list of costumes and produces a string
    which represents label of the last costume that is
    available in a medium. If there are no medium costumes return None.
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        str: The string indicating the label of the last costume
            that is size medium. 
    '''
    lastMedium = None
    for costume in costumes:
        for size in costume["sizes"]:
            if size == "M":
                lastMedium = costume["label"]
    return lastMedium

assert_equal(find_last_medium(MONSTER_MASH['costumes 2']), None)
assert_equal(find_last_medium(MONSTER_MASH['costumes 4']), "Captain America")
assert_equal(find_last_medium(MONSTER_MASH['costumes 5']), "Rogue")


'''
C7. Define a function `find_first_small` that consumes a list of costumes
and produces the label of the first costume that is available in a small.
If no small costumes are found, produce the special value `None`.
'''
def find_first_small(costumes: [Costume]) -> str:
    '''
    Consumes a list of costumes and produces a string
    which represents the label of the first costume that is
    available in a small. If there are no small costumes return None.
    
    Args:
        costumes ([Costume]): The list of costumes that is given.
    Returns:
        str: The string indicating the label of the first costume
            that is size small. 
    '''    
    for costume in costumes:
        if "S" in costume["sizes"]:
            small = costume["label"]
            return small
    return None

assert_equal(find_first_small(MONSTER_MASH['costumes 2']), None)
assert_equal(find_first_small(MONSTER_MASH['costumes 3']), "Mummy")
assert_equal(find_first_small(MONSTER_MASH['costumes 4']), "Spiderman")


## Tombstones

'''
A Grave is a dictionary with two keys:
* 'Name': A string value with the grave's occupant's name
* 'Message': A string value with the grave's message
'''

Grave = {'name': str, 'Message': str}


'''
G1. Define the function `count_grave_all` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Include spaces and new lines.
'''
def count_grave_all(graves: [Grave]) -> int:
    '''
    Consumes a list of graves and produces an integer value
    representing the number of characters neeeded to write
    the messages of the graves, including spaces and new lines.
    
    Args:
        graves ([Grave]): The list of graves that is given.
    Returns:
        int: The integer value indicating the number of characters needed
            to write all of the messages of the graves.
    '''
    total = 0
    for grave in graves:
        total = total + len(grave["message"])
    return total

assert_equal(count_grave_all(MONSTER_MASH['graves 1']), 149)
assert_equal(count_grave_all(MONSTER_MASH['graves 2']), 105)
assert_equal(count_grave_all(MONSTER_MASH['graves 3']), 108)


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
def estimate_grave_cost(graves: [Grave]) -> int:
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

assert_equal(estimate_grave_cost(MONSTER_MASH['graves 1']), 240)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 2']), 180)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 3']), 190)


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
    '''
    Consumes a list of medias and produces an integer value 
    representing the number of items that are less than
    100 minutes long. 
    
    Args:
        medias ([Media]): The list of medias that is given.
    Returns:
        int: The integer value indicating the number of items that
        are less than 100 minutes long. 
    '''
    count = 0
    for media in medias:
        if media["duration"] < 100:
            count = count + 1
    return count

assert_equal(count_not_long(MONSTER_MASH['media 2']), 4)
assert_equal(count_not_long(MONSTER_MASH['media 3']), 0)
assert_equal(count_not_long(MONSTER_MASH['media 4']), 2)


'''
E3. Define the function `take_until_long` that consumes a list of media
and counts elements until it encounters something that is 100 minutes
longer or more, and then stops and returns the number counted so far.
'''
def take_until_long(medias: [Media]) -> int:
    '''
    Consumes a list of medias and produces an integer value 
    representing the number of media until it encounters
    something 100 minutes or more, and then stops.
    
    Args:
        medias ([Media]): The list of medias that is given.
    Returns:
        int: The integer value indicating the number of media
            up until a media that is 100 minutes or more is encountered. 
    '''
    taking = True
    count = 0
    for media in medias:
        if media["duration"] >= 100:
            taking = False
        elif taking:
            count = count + 1
    return count
            
assert_equal(take_until_long(MONSTER_MASH['media 3']), 0)
assert_equal(take_until_long(MONSTER_MASH['media 4']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 1']), 2)


'''
E4. Define the function `longest_kind` that consumes a list of Media
and produces a string value representing the kind that had the highest
duration. If the list is empty, return the value None.
'''
def longest_kind(medias: [Media]) -> str:
    '''
    Consumes a list of medias and produces a string
    that represents the kind that has the highest duration. 
    
    Args:
        medias ([Media]): The list of medias that is given.
    Returns:
        str: The string indicating the kind with the highest duration. 
    '''
    if medias:
        maximum = 0
        for media in medias:
            if maximum < media["duration"]:
                maximum = media["duration"]
                longestKind = media["kind"]
        return longestKind
    else:
        return None

assert_equal(longest_kind(MONSTER_MASH['media 2']), "song")
assert_equal(longest_kind(MONSTER_MASH['media 3']), "game")
assert_equal(longest_kind(MONSTER_MASH['media 5']), None)


'''
E5. Define the function `same_kind_of_media` that consumes a list
of Media and produces a boolean indicating whether all of the
kinds of media are the same as each other. If the list is empty,
the result is True.
'''
def same_kind_of_media(medias: [Media]) -> bool:
    '''
    Consumes a list of medias and produces a boolean
    value that represents whether or not all of the medias
    are the same kind.
    
    Args:
        medias ([Media]): The list of medias that is given.
    Returns:
        bool: The boolean value indicating whether or not all
        of the medias are the same kind.
    '''
    if medias:
        result = True
        kind = medias[0]["kind"]
        for media in medias:
            if media["kind"] != kind:
                result = False
            else:
                kind = media["kind"]
        return result
    else:
        return True

assert_equal(same_kind_of_media(MONSTER_MASH['media 3']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 4']), False)
assert_equal(same_kind_of_media(MONSTER_MASH['media 5']), True)


## Brewing Potions

'''
An Ingredient has the following keys:
* 'name': The name of the ingredient
* 'rare?': Whether the ingredient is rare

A Potion has the following keys:
* 'effect': The effect of the potion
* 'ingredients': The required ingredients of the potion
* 'time required': How many minutes it takes to brew the potion
'''

Ingredient = {'name': str, 'rare?': bool}
Potion = {'effect': str, 'ingredients': [Ingredient], 'time required': int}


'''
B1. Define the function `total_ingredients` that consumes a list
of potions and produces the total number of required ingredients.
Include duplicates in your total.
'''
def total_ingredients(potions: [Potion]) -> int:
    '''
    Consumes a list of potions and produces an integer
    value that represents the total number of required ingredients.
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        int: The integer value indicating the total number of
            required ingredients. 
    '''
    total = 0
    for potion in potions:
        for ingredient in potion["ingredients"]:
            total = total + 1
    return total

assert_equal(total_ingredients(MONSTER_MASH['brewing 1']), 9)
assert_equal(total_ingredients(MONSTER_MASH['brewing 2']), 5)
assert_equal(total_ingredients(MONSTER_MASH['brewing 3']), 8)


'''
B2. Define the function `count_rare_ingredients` that consumes a list
of potions and produces the total number of required ingredients that
are rare.
'''
def count_rare_ingredients(potions: [Potion]) -> int:
    '''
    Consumes a list of potions and produces an integer
    value that represents the total number of required ingredients
    that are rare.
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        int: The integer value indicating the total number of
            required ingredients that are rare.
    '''
    total = 0
    for potion in potions:
        for ingredient in potion["ingredients"]:
            if ingredient["rare?"]:
                total = total + 1
    return total

assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 1']), 1)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 2']), 4)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 3']), 4)


'''
B3. Define the function `get_ingredients` that consumes a list of
potions and produces a list of strings (representing ingredient names)
in the order that the ingredients are listed in the potions.
Do not include duplicate ingredients.
'''
def get_ingredients(potions: [Potion]) -> [str]:
    '''
    Consumes a list of potions and produces a list of strings
    that represent the ingredient names in the order they are listed
    in the potions, and not including duplicate ingredients. 
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        [str]: The list of strings indicating the ingredient names
            without duplicate ingredients. 
    '''
    ingredList = []
    for potion in potions:
        for ingredient in potion["ingredients"]:
            if ingredient["name"] not in ingredList:
                ingredList.append(ingredient["name"])
    return ingredList

assert_equal(get_ingredients(MONSTER_MASH['brewing 1']), ["Spider Webs", "Ant Hill", "Dragon Egg", "Moon Blooms", "Candy Leaf"])
assert_equal(get_ingredients(MONSTER_MASH['brewing 2']), ["Dream Petal", "Hens Teeth", "Ant Hill"])
assert_equal(get_ingredients(MONSTER_MASH['brewing 3']), ["Candy Leaf", "Moon Blooms", "Red Nightshade", "Werewolf Heart"])


'''
B4. Define the function `get_brewing_time` that consumes a list of
potions and produces an integer representing the total time required
to brew all the potions.
'''
def get_brewing_time(potions: [Potion]) -> int:
    '''
    Consumes a list of potions and produces an integer
    representing the total time required to brew all the potions.
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        int: The integer value indicating the time required to brew all the potions.
    '''
    time = 0
    for potion in potions:
        time = time + potion["time required"]
    return time

assert_equal(get_brewing_time(MONSTER_MASH['brewing 1']), 15)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 2']), 16)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 3']), 12)


'''
B5. Define the function `brew_time_per_ingredient` that consumes a list
of potions and produces a float representing the average amount of
time spent brewing overall. To do so, add up the time spent brewing
and divide it by the number of ingredients. If there are no ingredients,
return the value None.
'''
def brew_time_per_ingredient(potions: [Potion]) -> float:
    '''
    Consumes a list of potions and produces a float
    value representing the average amount of time spent brewing
    overall. Return None if no ingredients. 
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        float: The float value indicating the average time spent brewing overall.
    '''
    if potions:
        time = get_brewing_time(potions)
        numIngredients = total_ingredients(potions)
        return time / numIngredients
    else:
        return None
    
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 2']), 3.2)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 3']), 1.5)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 4']), None)


'''
B6. Define the function `get_rarest_potion` that consumes a list of potions
and returns the effect of the potion that requires the most rare ingredients.
If there are no rare ingredients in any of the potions, then return None instead.
'''
def get_rarest_potion(potions: [Potion]) -> str:
    '''
    Consumes a list of potions and produces string representing
    the effect of the potion that requires the most rare ingredients.
    Return None if no rare ingredients in any of the potions.
    
    Args:
        potions ([Potion]): The list of potions that is given.
    Returns:
        str: The string indicating the effect of the potion that
            requires the most rare ingredients.
    '''
    if count_rare_ingredients(potions) == 0:
        return None
    else:
        numRares = []
        for potion in potions:
            rares = 0
            for ingredient in potion["ingredients"]:   
                if ingredient["rare?"]:
                    rares = rares + 1
            numRares.append(rares)
        
        maximum = 0
        count = -1
        for num in numRares:
            if maximum <= num:
                maximum = num
                count = count + 1
        
        effect = potions[count]["effect"]
        return effect
    
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 1']), "Sweet Breathing Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 2']), "Embiggening Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 4']), None)



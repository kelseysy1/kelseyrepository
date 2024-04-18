def most_popular_foods(fav_foods):

    '''
    Given a dictionary of people's favorite foods, return a new dictionary
    with food as the key and the list of people who like that food as the value.
    Example, given 
    fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 
    'Michelle': 'pasta', 'Patrick': 'pizza'})
    You should return the new dictionary 
    {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 
    'pasta': ['Michelle']}

    Steps
    Create an empty dictionary
    Iterate through the fav_foods dictionary
        if the food is NOT in the new dictionary:
            create an empty list and add the person to the list
            add the food as they key and the list as the value
        else:
            add the person to the list of people who favorite that food
    return dictionary
    '''

    #create empty dictionary to store result
    swapped_foods = {}
    
    
    #fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 
    #'Michelle': 'pasta', 'Patrick': 'pizza'}


    
    # Iterate through the fav_foods dictionary
    for person, food in fav_foods.items():
        # Check if the food is NOT in the new dictionary
        if food not in swapped_foods:
            # If not, create a new key-value pair with the food as the key
            # and a list containing the person as the value
            swapped_foods[food] = [person]
        else:
            # If the food is already a key, all you have to do is append the person to the existing list
            swapped_foods[food].append(person)

    # Return the final dictionary
    return swapped_foods


  





assert most_popular_foods(fav_foods={'Kathleen': 'pizza', 'Steve': 'burger', 'John': 'steak', 'Michelle': 'pasta', 'Patrick': 'pizza'}) == {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 'pasta': ['Michelle']}, "expected {'pizza': ['Kathleen', 'Patrick'], 'burger': ['Steve'], 'steak': ['John'], 'pasta': ['Michelle']}"
print("correct")
assert most_popular_foods({"Kathleen": "pizza", "Yin": "pizza", "Kearicia":"Italian","Owen": "burgers"}) == {'pizza': ['Kathleen', 'Yin'], 'Italian': ['Kearicia'], 'burgers': ['Owen']}, "expected {'pizza': ['Kathleen', 'Yin'], 'Italian': ['Kearicia'], 'burgers': ['Owen']}"
print("correct")
assert most_popular_foods({'Kathleen': 'pizza', 'Max':'burgers', 'Matt':'burgers', 'Andy':'pizza','Christina':'burgers'}) == {'pizza': ['Kathleen', 'Andy'], 'burgers': ['Max','Matt','Christina']}, "expected {'pizza': ['Kathleen', 'Andy'], 'burgers': ['Matt','Max','Christina']}"
print("correct")
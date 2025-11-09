def name_frequency(names):
    dict = {}
    arr = []
    nr = 0

    for i in range(len(names)):
        first_name = names[i].split() # Get the first name of the persons
        arr.append(first_name[0]) # Get all the first names into a list
        nr = arr.count(first_name[0]) # Count how many times it appears

        dict[first_name[0]] = nr # Set it into the dictionary, name, count
        
    return dict
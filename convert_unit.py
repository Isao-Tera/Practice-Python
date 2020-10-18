# Prepare a function to profile
def convert_units(heroes, weight, height):
    """
    convert units from lbs to ISO

    Arguments:
    heroes : name of hero
    weight: weight of hero
    height: height of hero

    Returns:
    hero_data: index and converted data
    """

    new_hts = [ht * 0.39370 for ht in height]
    new_wts = [wt * 2.20462 for wt in weight]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

    # Modify the function by changing bottleneck
def convert_units_broadcast(heroes, weight, height):
    """
    convert units from lbs to ISO

    Arguments:
    heroes : name of hero
    weight: weight of hero
    height: height of hero

    Returns:
    hero_data: index and converted data
    """

    # Change list comprihension to np.array 
    new_hts = height * 0.39370
    new_wts = weight * 2.20462 

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data
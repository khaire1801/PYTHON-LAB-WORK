def determine_class(age):
    
    if 2 <= age < 3:
        return "Eligible for Playgroup"
    elif 3 <= age < 4:
        return "Eligible for Nursery"
    elif 4 <= age < 5:
        return "Eligible for Jr. KG"
    elif 5 <= age < 6:
        return "Eligible for Sr. KG"
    else:
        return "Not eligible for Playgroup, Nursery, Jr. KG, or Sr. KG"
    

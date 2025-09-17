#defining cases 
def day_of_the_week(day):
    if day == 1:
        return("monday")
    elif day == 2:
        return("tuesday")
    elif day == 3:
        return("wenesday")
    elif day == 4:
        return("thursday")
    elif day == 5:
        return("friday")
    elif day == 6:
        return("saturday")
    elif day == 7:
        return("sunday")
    else : # none of the above 
        return("Error")

print(day_of_the_week(2))

#match case replacing if and else (case) and elif (case) 
def day_of_the_week(day):
    match day:
        case 1:
            return("monday")
        case 2:
            return("tuesday")
        case 3:
            return("wenesday")
        case 4:
            return("thursday")
        case 5:
            return("friday")
        case 6:
            return("saturday")
        case 7:
            return("sunday")
        case _: # none of the above 
            return("Error")

print(day_of_the_week(8))
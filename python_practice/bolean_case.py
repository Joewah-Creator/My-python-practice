#match case replacing if and else (case) and elif (case) 
def is_weekday (day):
    match day: 
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return("true")
        case "saturday" | "sunday":
            return("false")
        case _: # none of the above 
            return("Error")

print(is_weekday("saturday"))
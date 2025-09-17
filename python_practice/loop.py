# loop with syntax and use cases
def is_weekend (day):
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return("false")
        case "saturday" | "sunday":
            return("true")
print(is_weekend("monday"))

# loop_for_days
#example one
weekdays = ("monday" , "tuesday" , "wednesday" , "thursday" , "friday")
is_weekend = ("saturday" , "sunday")
for day in weekdays :
    print(day)

# Example two
for day in is_weekend :
    print(day)

# example 3
odd = 3,5,7,9
even = 2,4,6,8,10
for number in odd :
    print(number)
for number in even :
    print(number)

# example 4
numbers = 2 , 21 , 9 ,13 , 18 , 6
total = 0
# use for loop and add each number to total
for number in numbers :
    total = total + number 

print(total) #sum of all the numbers
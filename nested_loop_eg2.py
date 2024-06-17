# Count the occurance of a letter in a list
# Initialise a list of strings
# Set result variable to zero to start an operation.

string_list = ["Academy","Champion","Coder"]
result = 0

# Check strings for letter "C"
# First check for variable string inside of string_list
# Second check for variable letter inside strings
# Third if the variable letter contains "Cc" add +1 to result variable
# Use in instead of == Cc because you are dealing with alphabeth 

for string in string_list:
    for letter in string:
        if letter in "Cc":
            result += 1
# Make sure you go outside loop to print result           
print("The total accurance of letter C is",result) 
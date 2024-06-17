# t1w6-Saturday

## Perform calculation using If, else statements

# Lists
* Composite data type = multiple data types can be stored in one variable
* Each piece is called element
* You can access elements in the list index, index starts at 0.
e.g:
countries = ["Brazil", "Australia", "Fiji"]

print(countries[2])

The printed output will be "Fiji"

* Remove data = .remove
* Add data = .append
* Count length .len

# Loops
Used to repeat a block of codes multiple times until a certain condition is met.

DRY coding principle: Don't repeat yourself.

Loops = how many times the user wants to run the intended block.

IF STATEMENT = If condition would decide wether or not to run the intended block.

# While loop
While the condition is met, keep executing the intended block, if not met, skip the block.
* Make sure program can meet condition to enter the loop
* Make sure program can meet condition to exit the loop


# For loops
For each element in the list, execute the intended statement block.

for variable_name in sequence:
    execute this

# Range
It's a pre-defined function that generates a sequence of numbers, it's useful in LOOPS for
iterating a specific number of times over a sequence of numbers.

range(start, stop, step)

# Loop control statements
Control the flow of the loop, terminate the loop earlier if you want to or skip over some interaction.

## Break statement
Terminates the loop immediately, it moves to the next statement after the loop.

## Continue statement
Skips the rest of the code inside of the loop for current interaction and moves to the next interaction.

# Nested loops
A loop inside another loop. It's useful for running over multi dimensional structures like MATRIX.

# Enumerate() function
Used to access the index and the value of elements of the list using two variables in the FOR loop.

# Lists
They can store different values
e.g list contains integer and string

random_list = [1,150,"Jess",3]
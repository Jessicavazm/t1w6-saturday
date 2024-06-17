# Breaking the loop using BREAK, in this case program exit out completely of the loop after the break statement.


# i = 0

# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# Breaking the loop using CONTINUE, it only skips the rest of the code for the current interaction and then moves on to the next loop interaction.

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# Skipping vowels in a text

# text = "Coder Academy"
# vowels = "aeiouAEIOU"

# for each in text:
#     if each in vowels:
#         continue
#     print(each, end="")
# print()

# Stop using break condition
# Stop on stop signal

signals = ["Start", "Go", "Stop", "Start"]

for each in signals:
    if each == "Stop":
        break
    else:
        print(each)
# animals = ["cat", "dog", "horse", "pug"]

# for index,animal in enumerate (animals):
#     print(f"{index}: {animal}")

# Find index for Cherry

fruits = ["banana", "cherry","Apple"]
target = "cherry"

for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"Found {target} in index {index}.")
        break

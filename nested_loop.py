matrix = [[1,2,3],[4,5,6],[7,8,9]]

# print(matrix[0][2])

# Print all items in all list using FOR and IN:
# end=" " prints lists in horizontal line and with a space between numbers
# print() ensure that next row(list) starts on new line

for rows in matrix:
    for item in rows:
        print(item, end=" ")
    print()

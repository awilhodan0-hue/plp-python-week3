count = 1
total = 0

# BUG: Added the missing colon after the while condition.
# BUG: Changed < to <= so the loop includes the number 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total to a string so it can be joined with the text.
print("Sum of 1 to 5 is: " + str(total))

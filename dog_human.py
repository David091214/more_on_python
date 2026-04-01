
dog_age = int(input())


if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = 21 + (dog_age - 2) * 4

# Print the result as integer
print(int(human_age))